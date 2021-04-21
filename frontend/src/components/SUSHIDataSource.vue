<template>
  <v-data-table
    :headers="headerData"
    :items="results"
    // :items-per-page="5"
    class="elevation-1"
    v-bind:loading="is_loading"
    loading-text="Loading... Please wait"
  >
      <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>My CRUD</v-toolbar-title>
        <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider>
        <v-spacer></v-spacer>
        <v-dialog
          v-model="dialog"
          max-width="500px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
            >
              New Item
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.id"
                      label="Database ID"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-checkbox
                      label="Active"
                      v-model="editedItem.active"
                    ></v-checkbox>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.inactive_date"
                      label="Inactive Date"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.name"
                      label="Name"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.identifier"
                      label="Unique Identifier"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue darken-1"
                text
                @click="close"
              >
                Cancel
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="save"
              >
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="headline">Are you sure you want to delete this item?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
              <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
    <template v-slot:no-data>
      <v-btn
        color="primary"
        @click="initialize"
      >
        Reset
      </v-btn>
    </template>
    </v-data-table>
</template>

<script>
const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay))

  export default {
    data () {
      return {
        is_loading: false,
        total: -1,
        results: [],
        headerData: [],
        dialog: false,
        dialogDelete: false,
        editedIndex: -1,
        editedItem: {
          id: "",
          active: true,
          inactive_date: "",
          name: "",
          identifier: "",
          description: "",
          contact: "",
          status: "",
          url_template: "",
          requester_id: "",
          customer_id: "",
          requester_name: "",
          customer_name: "",
          user_name: "",
          password: "",
          requester_email: "",
          api_key: "",
          platform: "R5"
        },
        defaultItem: {
          id: "",
          active: true,
          inactive_date: "",
          name: "",
          identifier: "",
          description: "",
          contact: "",
          status: "",
          url_template: "",
          requester_id: "",
          customer_id: "",
          requester_name: "",
          customer_name: "",
          user_name: "",
          password: "",
          requester_email: "",
          api_key: "",
          platform: "R5"
        },
      }
    },

    async created () {
      this.is_loading = true
      let sd = await fetch("/api/sushidatasource")
      let js = await sd.json()

      this.total = js.total
      this.results = js.results
      this.headerData = js.headerData

      this.is_loading = false
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
      },
    },

    methods: {
      editItem (item) {
        this.editedIndex = this.results.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

    deleteItem (item) {
      this.editedIndex = this.results.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },

    deleteItemConfirm () {
      this.results.splice(this.editedIndex, 1)
      this.closeDelete()
    },

    close () {
      this.dialog = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

    closeDelete () {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

    save () {
      if (this.editedIndex > -1) {
        Object.assign(this.results[this.editedIndex], this.editedItem)
      } else {
        this.results.push(this.editedItem)
      }
      this.close()
    },
  }
  }
</script>
