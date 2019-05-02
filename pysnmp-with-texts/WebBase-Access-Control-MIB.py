#
# PySNMP MIB module WebBase-Access-Control-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WebBase-Access-Control-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:39:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, Unsigned32, Counter64, ModuleIdentity, Integer32, TimeTicks, MibIdentifier, IpAddress, ObjectIdentity, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "Unsigned32", "Counter64", "ModuleIdentity", "Integer32", "TimeTicks", "MibIdentifier", "IpAddress", "ObjectIdentity", "Counter32", "Bits")
TextualConvention, RowStatus, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "MacAddress")
class VlanId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

swWACMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 27))
if mibBuilder.loadTexts: swWACMIB.setLastUpdated('0907200000Z')
if mibBuilder.loadTexts: swWACMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: swWACMIB.setContactInfo('http://support.dlink.com')
if mibBuilder.loadTexts: swWACMIB.setDescription('.')
swWACCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 27, 1))
swWACInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 27, 2))
swWACMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 27, 3))
swWebAuthAdminState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWebAuthAdminState.setStatus('current')
if mibBuilder.loadTexts: swWebAuthAdminState.setDescription('This object enables/disables the web-based authentication status of the device.')
swWebAuthMethod = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("radius", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWebAuthMethod.setStatus('current')
if mibBuilder.loadTexts: swWebAuthMethod.setDescription('This object indicates the authentication method type. The RADIUS method is authenticated per authentication server.')
swWebAuthVlanName = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWebAuthVlanName.setStatus('obsolete')
if mibBuilder.loadTexts: swWebAuthVlanName.setDescription('This object indicates the authentication method VLAN name.')
swWebAuthAllPortstate = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWebAuthAllPortstate.setStatus('obsolete')
if mibBuilder.loadTexts: swWebAuthAllPortstate.setDescription('This object enables/disables the authentication state of all ports on the device.')
swWebAuthDefaultredirpath = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWebAuthDefaultredirpath.setStatus('current')
if mibBuilder.loadTexts: swWebAuthDefaultredirpath.setDescription('The URL that the client will be redirected to after successful authentication. Initially, the redirected path is an empty string. It must be specified by the user before the function can be enabled.')
swWebAuthLogouttimer = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWebAuthLogouttimer.setStatus('obsolete')
if mibBuilder.loadTexts: swWebAuthLogouttimer.setDescription('The authenticated port will revert to an un-authenticated state after the logout times out. When the value is 0, it means the logout timer is infinite and the authenticated port will never revert to an un-authenticated state. The default value is 60 minutes. ')
swWACVirtualIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWACVirtualIpAddr.setStatus('current')
if mibBuilder.loadTexts: swWACVirtualIpAddr.setDescription('Specifies the WAC virtual IP address which is used to accept authentication requests from an unauthenticated host. The virtual IP of WAC is used to accept authentication requests from an unauthenticated host. Only requests sent to this IP will get a correct response. NOTE: This IP does not respond to ARP requests or ICMP packets. ')
swWACSwitchHttpProtocol = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("http", 1), ("https", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWACSwitchHttpProtocol.setStatus('current')
if mibBuilder.loadTexts: swWACSwitchHttpProtocol.setDescription('Specifies which WAC protocol runs on this TCP port.')
swWACSwitchHttpPort = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWACSwitchHttpPort.setStatus('current')
if mibBuilder.loadTexts: swWACSwitchHttpPort.setDescription('Specifies the TCP port which the WAC switch listens to and uses to finish the authenticating process.')
swWACAuthFailOverState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWACAuthFailOverState.setStatus('current')
if mibBuilder.loadTexts: swWACAuthFailOverState.setDescription('This object enables/disables the web-based authentication auth_failover status of the device. When the authentication failover is enabled, if RADIU servers authentication are unreachable, the local database will be used to do the authentication.')
swWACRadiusAuthorizationState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWACRadiusAuthorizationState.setStatus('current')
if mibBuilder.loadTexts: swWACRadiusAuthorizationState.setDescription('This object enables/disables the web-based authentication RADIUS authorization status of the device. When the RADIUS authorization state is disabled, the assigned information from the RADIUS server will be ignored.')
swWACLocalAuthorizationState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWACLocalAuthorizationState.setStatus('current')
if mibBuilder.loadTexts: swWACLocalAuthorizationState.setDescription('This object enables/disables the web-based authentication local authorization status of the device. When the local authorization state is disabled, the assigned information from the local database will be ignored.')
swWACAuthClearDefaultredirpath = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("start", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWACAuthClearDefaultredirpath.setStatus('current')
if mibBuilder.loadTexts: swWACAuthClearDefaultredirpath.setDescription('This object is used to clear the default redirect URL that has been previously configured.')
swWACVirtualIPv6Addr = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 14), Ipv6Address()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWACVirtualIPv6Addr.setStatus('current')
if mibBuilder.loadTexts: swWACVirtualIPv6Addr.setDescription('Specifies the WAC virtual IPv6 address which is used to accept authentication requests from an unauthenticated host. The virtual IP of WAC is used to accept authentication requests from an unauthenticated host. Only requests sent to this IP will get a correct response. NOTE: This IP does not respond to ARP requests or ICMP packets. ')
swWACAuthInfoTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 1), )
if mibBuilder.loadTexts: swWACAuthInfoTable.setStatus('current')
if mibBuilder.loadTexts: swWACAuthInfoTable.setDescription('This table contains WAC client host information.')
swWACAuthInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 1, 1), ).setIndexNames((0, "WebBase-Access-Control-MIB", "swWACAuthInfoPort"), (0, "WebBase-Access-Control-MIB", "swWACAuthInfoAuthStatus"), (0, "WebBase-Access-Control-MIB", "swWACAuthInfoMACAddr"))
if mibBuilder.loadTexts: swWACAuthInfoEntry.setStatus('current')
if mibBuilder.loadTexts: swWACAuthInfoEntry.setDescription('This list contains WAC client host information.')
swWACAuthInfoPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWACAuthInfoPort.setStatus('current')
if mibBuilder.loadTexts: swWACAuthInfoPort.setDescription('Specifies the WAC host port number.')
swWACAuthInfoAuthStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("authenticated", 1), ("authenticating", 2), ("blocked", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWACAuthInfoAuthStatus.setStatus('current')
if mibBuilder.loadTexts: swWACAuthInfoAuthStatus.setDescription('Specifies the WAC host Authentication state.')
swWACAuthInfoMACAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWACAuthInfoMACAddr.setStatus('current')
if mibBuilder.loadTexts: swWACAuthInfoMACAddr.setDescription('Specifies the WAC host MAC address.')
swWACAuthInfoVID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 1, 1, 4), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWACAuthInfoVID.setStatus('current')
if mibBuilder.loadTexts: swWACAuthInfoVID.setDescription('Specifies the WAC host VID.')
swWACAuthInfoRemainAgeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWACAuthInfoRemainAgeTime.setStatus('current')
if mibBuilder.loadTexts: swWACAuthInfoRemainAgeTime.setDescription('Specifies the remaining WAC host agetime. 0 indicates the authenticated host on the port will never age out. ')
swWACAuthInfoIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWACAuthInfoIdleTime.setStatus('current')
if mibBuilder.loadTexts: swWACAuthInfoIdleTime.setDescription('Specifies the WAC host idle time. 0 indicates the idle state of the authenticated host on the port will never be checked. ')
swWACAuthInfoBlockTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWACAuthInfoBlockTime.setStatus('current')
if mibBuilder.loadTexts: swWACAuthInfoBlockTime.setDescription('Specifies the WAC host block time.')
swWACAuthInfoStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWACAuthInfoStatus.setStatus('current')
if mibBuilder.loadTexts: swWACAuthInfoStatus.setDescription('Specifies the status of the WAC host. Setting delete (2) will delete this WAC host entry. ')
swWACAuthInfoPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWACAuthInfoPriority.setStatus('current')
if mibBuilder.loadTexts: swWACAuthInfoPriority.setDescription('Specifies the WAC host priority assigned when pass authentication. -1 indicates the host has no priority assigned.')
swWACAuthStateTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 2), )
if mibBuilder.loadTexts: swWACAuthStateTable.setStatus('current')
if mibBuilder.loadTexts: swWACAuthStateTable.setDescription('This table contains WAC client host information.')
swWACAuthStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 2, 1), ).setIndexNames((0, "WebBase-Access-Control-MIB", "swWACAuthStatePort"), (0, "WebBase-Access-Control-MIB", "swWACAuthStateOriginalVid"), (0, "WebBase-Access-Control-MIB", "swWACAuthStateMACAddr"))
if mibBuilder.loadTexts: swWACAuthStateEntry.setStatus('current')
if mibBuilder.loadTexts: swWACAuthStateEntry.setDescription('This list contains WAC client host information.')
swWACAuthStatePort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWACAuthStatePort.setStatus('current')
if mibBuilder.loadTexts: swWACAuthStatePort.setDescription('Specifies the WAC host port number.')
swWACAuthStateOriginalVid = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 2, 1, 2), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWACAuthStateOriginalVid.setStatus('current')
if mibBuilder.loadTexts: swWACAuthStateOriginalVid.setDescription('Specifies the WAC host original receive VLAN ID.')
swWACAuthStateMACAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 2, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWACAuthStateMACAddr.setStatus('current')
if mibBuilder.loadTexts: swWACAuthStateMACAddr.setDescription('Specifies the WAC host MAC address.')
swWACAuthStateAuthStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("authenticated", 1), ("authenticating", 2), ("blocked", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWACAuthStateAuthStatus.setStatus('current')
if mibBuilder.loadTexts: swWACAuthStateAuthStatus.setDescription('Specifies the WAC host Authentication state.')
swWACAuthStateAssignVid = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 2, 1, 7), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWACAuthStateAssignVid.setStatus('current')
if mibBuilder.loadTexts: swWACAuthStateAssignVid.setDescription('Specifies the WAC host assign VID.')
swWACAuthStateAssignPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWACAuthStateAssignPriority.setStatus('current')
if mibBuilder.loadTexts: swWACAuthStateAssignPriority.setDescription('Specifies the WAC host priority assigned when pass authentication. -1 indicates the host has no priority assigned.')
swWACAuthStateRemainTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWACAuthStateRemainTime.setStatus('current')
if mibBuilder.loadTexts: swWACAuthStateRemainTime.setDescription('Specifies the remaining WAC host aging time/ block time. 0 indicates the authenticated host on the port will never age out. ')
swWACAuthStateIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWACAuthStateIdleTime.setStatus('current')
if mibBuilder.loadTexts: swWACAuthStateIdleTime.setDescription('Specifies the WAC host idle time. 0 indicates the idle state of the authenticated host on the port will never be checked. ')
swWACAuthStateDelAction = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 2, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWACAuthStateDelAction.setStatus('current')
if mibBuilder.loadTexts: swWACAuthStateDelAction.setDescription('Used to delete the specified authentication entry. Setting delete(2) will delete this WAC host entry. ')
swWebAuthPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 1), )
if mibBuilder.loadTexts: swWebAuthPortTable.setStatus('current')
if mibBuilder.loadTexts: swWebAuthPortTable.setDescription('A table that contains method and state information for every port.')
swWebAuthPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 1, 1), ).setIndexNames((0, "WebBase-Access-Control-MIB", "swWebAuthPortIndex"))
if mibBuilder.loadTexts: swWebAuthPortEntry.setStatus('current')
if mibBuilder.loadTexts: swWebAuthPortEntry.setDescription('A list of method types and states for each port.')
swWebAuthPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWebAuthPortIndex.setStatus('current')
if mibBuilder.loadTexts: swWebAuthPortIndex.setDescription("This object indicates the module's port number.")
swWebAuthPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWebAuthPortState.setStatus('current')
if mibBuilder.loadTexts: swWebAuthPortState.setDescription('This object enables/disables the authentication state of this port.')
swWebAuthPortUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWebAuthPortUserName.setStatus('obsolete')
if mibBuilder.loadTexts: swWebAuthPortUserName.setDescription('This object indicates the user name of the port.')
swWebAuthAuthStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unauthenticated", 1), ("authenticated", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWebAuthAuthStatus.setStatus('obsolete')
if mibBuilder.loadTexts: swWebAuthAuthStatus.setDescription('This object indicates whether the current port is authenticated or not.')
swWebAuthAssignedVID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWebAuthAssignedVID.setStatus('obsolete')
if mibBuilder.loadTexts: swWebAuthAssignedVID.setDescription('This object indicates the assigned VLAN ID of this port.')
swWACPortAgeingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWACPortAgeingTime.setStatus('current')
if mibBuilder.loadTexts: swWACPortAgeingTime.setDescription('Specifies the time period during which an authenticated host will remain in the authenticated state. 0 indicates the authenticated host will never age out on the port. ')
swWACPortIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWACPortIdleTime.setStatus('current')
if mibBuilder.loadTexts: swWACPortIdleTime.setDescription('Specifies the idle_time. If there is no traffic during idle_time, the host will be moved back to the unauthenticated state. 0 indicates the idle state of the authenticated host on the port will never be checked. ')
swWACPortBlockTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWACPortBlockTime.setStatus('current')
if mibBuilder.loadTexts: swWACPortBlockTime.setDescription('Specifies the block_time. If a host fails to pass authentication, it will be blocked for a period specified by the block_time. ')
swWebAuthUserTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 2), )
if mibBuilder.loadTexts: swWebAuthUserTable.setStatus('current')
if mibBuilder.loadTexts: swWebAuthUserTable.setDescription('A table that contains web-based authentication account info.')
swWebAuthUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 2, 1), ).setIndexNames((0, "WebBase-Access-Control-MIB", "swWebAuthUserNameIndex"))
if mibBuilder.loadTexts: swWebAuthUserEntry.setStatus('current')
if mibBuilder.loadTexts: swWebAuthUserEntry.setDescription('A list that contains web-based authentication account info.')
swWebAuthUserNameIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWebAuthUserNameIndex.setStatus('current')
if mibBuilder.loadTexts: swWebAuthUserNameIndex.setDescription('This object indicates the username with 15 being the maximum number of characters.')
swWebAuthUserPWD = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swWebAuthUserPWD.setStatus('current')
if mibBuilder.loadTexts: swWebAuthUserPWD.setDescription('This object indicates the password (maximum number of characters is 15) for this user account. It is write-only.')
swWebAuthUserVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swWebAuthUserVlanName.setStatus('obsolete')
if mibBuilder.loadTexts: swWebAuthUserVlanName.setDescription('This object indicates the VLAN name for this user account.')
swWebAuthUserStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swWebAuthUserStatus.setStatus('current')
if mibBuilder.loadTexts: swWebAuthUserStatus.setDescription('This object manages this entry.')
swWebAuthUserVID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swWebAuthUserVID.setStatus('current')
if mibBuilder.loadTexts: swWebAuthUserVID.setDescription('This object indicates the VID for this user account. 0 indicates to delete configure VID in this user account.')
mibBuilder.exportSymbols("WebBase-Access-Control-MIB", swWACSwitchHttpProtocol=swWACSwitchHttpProtocol, swWACRadiusAuthorizationState=swWACRadiusAuthorizationState, swWebAuthAuthStatus=swWebAuthAuthStatus, swWACAuthInfoBlockTime=swWACAuthInfoBlockTime, swWebAuthUserPWD=swWebAuthUserPWD, swWebAuthUserNameIndex=swWebAuthUserNameIndex, swWACAuthInfoPort=swWACAuthInfoPort, swWACAuthInfoIdleTime=swWACAuthInfoIdleTime, swWebAuthUserVlanName=swWebAuthUserVlanName, swWACMIB=swWACMIB, swWACAuthInfoEntry=swWACAuthInfoEntry, swWACAuthStateAuthStatus=swWACAuthStateAuthStatus, swWebAuthAdminState=swWebAuthAdminState, swWACAuthStateAssignVid=swWACAuthStateAssignVid, PYSNMP_MODULE_ID=swWACMIB, swWACAuthStateOriginalVid=swWACAuthStateOriginalVid, swWebAuthPortState=swWebAuthPortState, swWACAuthStateEntry=swWACAuthStateEntry, swWACSwitchHttpPort=swWACSwitchHttpPort, swWebAuthPortIndex=swWebAuthPortIndex, swWebAuthDefaultredirpath=swWebAuthDefaultredirpath, swWebAuthAssignedVID=swWebAuthAssignedVID, swWACAuthStatePort=swWACAuthStatePort, swWebAuthAllPortstate=swWebAuthAllPortstate, swWACAuthStateAssignPriority=swWACAuthStateAssignPriority, swWebAuthUserEntry=swWebAuthUserEntry, swWACCtrl=swWACCtrl, swWACLocalAuthorizationState=swWACLocalAuthorizationState, swWebAuthMethod=swWebAuthMethod, swWACAuthInfoAuthStatus=swWACAuthInfoAuthStatus, swWebAuthPortEntry=swWebAuthPortEntry, swWACInfo=swWACInfo, swWebAuthLogouttimer=swWebAuthLogouttimer, swWACAuthInfoVID=swWACAuthInfoVID, swWACPortBlockTime=swWACPortBlockTime, VlanId=VlanId, swWACAuthStateRemainTime=swWACAuthStateRemainTime, swWACPortIdleTime=swWACPortIdleTime, swWACAuthStateIdleTime=swWACAuthStateIdleTime, swWACAuthFailOverState=swWACAuthFailOverState, swWACVirtualIpAddr=swWACVirtualIpAddr, swWACVirtualIPv6Addr=swWACVirtualIPv6Addr, swWACAuthInfoStatus=swWACAuthInfoStatus, swWACAuthStateMACAddr=swWACAuthStateMACAddr, swWACPortAgeingTime=swWACPortAgeingTime, swWebAuthUserVID=swWebAuthUserVID, swWACAuthInfoPriority=swWACAuthInfoPriority, swWACAuthStateDelAction=swWACAuthStateDelAction, swWebAuthVlanName=swWebAuthVlanName, swWACAuthInfoTable=swWACAuthInfoTable, swWebAuthUserStatus=swWebAuthUserStatus, swWACAuthInfoMACAddr=swWACAuthInfoMACAddr, swWebAuthPortTable=swWebAuthPortTable, swWACAuthInfoRemainAgeTime=swWACAuthInfoRemainAgeTime, swWACMgmt=swWACMgmt, swWACAuthClearDefaultredirpath=swWACAuthClearDefaultredirpath, swWebAuthUserTable=swWebAuthUserTable, swWACAuthStateTable=swWACAuthStateTable, swWebAuthPortUserName=swWebAuthPortUserName)
