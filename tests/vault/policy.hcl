# For pytest
### For the correct receipt of the token via approle
path "auth/token/lookup" {
  capabilities = ["read"]
}

# For pytest
### To revoke the token after creating and testing approle
path "auth/token/revoke" {
  capabilities = ["update"]
}

# For pytest
### To read and update the namespace configuration
path "pytests/config" {
  capabilities = ["read", "list", "update"]
}

# For pytest
### To work with secret apllication data
path "pytests/data/configuration/*" {
  capabilities = ["create", "read", "update", "list"]
}

######

# For module
### To lookup for a token that has expired
path "auth/token/lookup-self" {
  capabilities = ["read"]
}

# For module
### To work with secret apllication data
path "myapp-1/data/configuration/*" {
  capabilities = ["read", "list"]
}
