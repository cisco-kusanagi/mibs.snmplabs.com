#
# PySNMP MIB module Wellfleet-BOOTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-BOOTP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:39:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ObjectIdentity, TimeTicks, Bits, ModuleIdentity, Unsigned32, Gauge32, MibIdentifier, iso, IpAddress, Counter32, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "TimeTicks", "Bits", "ModuleIdentity", "Unsigned32", "Gauge32", "MibIdentifier", "iso", "IpAddress", "Counter32", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfBootpGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfBootpGroup")
wfBootpClientGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 1))
wfBootpServerGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 2))
wfBootpRelayAgentGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3))
wfBootpRelayIntfTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1), )
if mibBuilder.loadTexts: wfBootpRelayIntfTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfTable.setDescription('This table contains per-interface configuration information for BOOTP relay agent operation')
wfBootpRelayIntfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1), ).setIndexNames((0, "Wellfleet-BOOTP-MIB", "wfBootpRelayIntfAddress"))
if mibBuilder.loadTexts: wfBootpRelayIntfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfEntry.setDescription('a BOOTP relay agent interface description')
wfBootpRelayIntfDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBootpRelayIntfDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfDelete.setDescription('Create/Delete: if set to delete, the BOOTP relay agent is removed from this network interface')
wfBootpRelayIntfDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBootpRelayIntfDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfDisable.setDescription('Enable/Disable: controls whether the BOOTP relay agent is enabled or disabled on this network interface')
wfBootpRelayIntfState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("invalid", 4), ("notpres", 5))).clone('notpres')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpRelayIntfState.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfState.setDescription('the state if the BOOTP relay agent on this interface')
wfBootpRelayIntfAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpRelayIntfAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfAddress.setDescription('network interface address')
wfBootpRelayIntfHops = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBootpRelayIntfHops.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfHops.setDescription('maximum hop count. BOOTREQUESTs with a larger hops field will be dropped')
wfBootpRelayIntfSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBootpRelayIntfSeconds.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfSeconds.setDescription('minimum seconds. BOOTREQUESTs with a smaller seconds field will be dropped')
wfBootpRelayIntfOpDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpRelayIntfOpDrops.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfOpDrops.setDescription('the total number of BOOTP packets received on this interface that were dropped because of an invalid operation field')
wfBootpRelayIntfRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpRelayIntfRequests.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfRequests.setDescription('the total number of BOOTREQUEST packets received on this interface')
wfBootpRelayIntfTranReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpRelayIntfTranReqs.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfTranReqs.setDescription('the total number of forwarded BOOTREQUEST packets received on this interface that contained a non-zero value in the gateway IP address field. This interface did not act as a relay agent for these packets')
wfBootpRelayIntfHopsDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpRelayIntfHopsDrops.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfHopsDrops.setDescription('the total number of forwarded BOOTREQUEST packets received on this interface that were dropped due to a hops field that was too large')
wfBootpRelayIntfBcastDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpRelayIntfBcastDrops.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfBcastDrops.setDescription('the total number of forwarded BOOTREQUEST packets received on this interface that were dropped due to a destination IP address that was not 255.255.255.255')
wfBootpRelayIntfSecDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpRelayIntfSecDrops.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfSecDrops.setDescription('the total number of forwarded BOOTREQUEST packets received on this interface that were dropped due to a seconds field that was too small')
wfBootpRelayIntfReplies = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpRelayIntfReplies.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfReplies.setDescription('the total number of BOOTPREPLY packets received that were addressed to this interface')
wfBootpRelayIntfGiaddrDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpRelayIntfGiaddrDrops.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfGiaddrDrops.setDescription("the total number of BOOTPREPLY packets received that were addressed to this interface and dropped because the giaddr field was not the same as the interface's address")
wfBootpRelayIntfResrcDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpRelayIntfResrcDrops.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfResrcDrops.setDescription('the total number of BOOTPREPLY packets received that were addressed to this interface and dropped because sufficient resources were not available')
wfBootpRelayIntfPassThroughMode = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("bootp", 1), ("bootp-dhcp", 2), ("dhcp", 3))).clone('bootp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBootpRelayIntfPassThroughMode.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfPassThroughMode.setDescription('The ACCEPTANCE mode for this interface: Bootp Requests only, both Bootp Requests and Bootp Requests containing DHCP messages, or Bootp Requests containing DHCP messages only.')
wfBootpRelayIntfUdpSktDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpRelayIntfUdpSktDrops.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfUdpSktDrops.setDescription('The total number of BOOTP packets received that were addressed to this interface and dropped because the UDP socket field is not BOOTPS (67).')
wfBootpRelayIntfTooShortDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpRelayIntfTooShortDrops.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfTooShortDrops.setDescription('The total number of BOOTP packets received that were addressed to this interface and dropped because the UDP length field is too short.')
wfBootpRelayIntfFltrDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpRelayIntfFltrDrops.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfFltrDrops.setDescription('The total number of BOOTPREQUEST packets received that were addressed to this interface and dropped because this type of packet is filtered off by the Pass Through Mode')
wfBootpRelayIntfPri = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBootpRelayIntfPri.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfPri.setDescription('Indicates priority of the interface on a multinetted interface')
wfBootpRelayIntfDhcpSvrDsbl = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBootpRelayIntfDhcpSvrDsbl.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfDhcpSvrDsbl.setDescription('Enable/Disable: controls whether the DHCP Server is enabled or disabled on this network interface.')
wfBootpRelayIntfDhcpSvDnDrps = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpRelayIntfDhcpSvDnDrps.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfDhcpSvDnDrps.setDescription('The total number of BOOTPREQUEST packets received that were addressed to this interface and dropped because this packet was a DHCP packet that should have been handled by the DHCP Server subsystem, but the subsystem was down.')
wfBootpRelayIntfArpCache = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBootpRelayIntfArpCache.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfArpCache.setDescription('Enable/Disable: controls whether the BOOTP relay agent will add/update an ARP entry based on the information contained in a BOOTP reply message (not applicable for DHCP)')
wfBootpRelayIntfBufLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 1000)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBootpRelayIntfBufLimit.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfBufLimit.setDescription('The total unprocessed number of BOOTP/DHCP request/reply packets allowed in this interface. See CR147895-1 for detail')
wfBootpRelayIntfBufDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpRelayIntfBufDrops.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayIntfBufDrops.setDescription('The total number of BOOTP request/reply packets dropped due to the wfBootpRelayIntfBufLimit is arrived.')
wfBootpRelayFwdTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 2), )
if mibBuilder.loadTexts: wfBootpRelayFwdTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayFwdTable.setDescription('for a BOOTP relay agent on a given interface, this table contains the list of interfaces through which that agent will forward BOOTREQUEST packets')
wfBootpRelayFwdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 2, 1), ).setIndexNames((0, "Wellfleet-BOOTP-MIB", "wfBootpRelayFwdAgentIntf"), (0, "Wellfleet-BOOTP-MIB", "wfBootpRelayFwdOutIntf"))
if mibBuilder.loadTexts: wfBootpRelayFwdEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayFwdEntry.setDescription('a BOOTP forwarding description')
wfBootpRelayFwdDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBootpRelayFwdDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayFwdDelete.setDescription('Create/Delete: if set to delete, the forwarding entry is removed from the table')
wfBootpRelayFwdDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBootpRelayFwdDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayFwdDisable.setDescription('Enable/Disable: controls whether the the forwarding entry is active or not')
wfBootpRelayFwdAgentIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpRelayFwdAgentIntf.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayFwdAgentIntf.setDescription("relay agent's network interface address")
wfBootpRelayFwdOutIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpRelayFwdOutIntf.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayFwdOutIntf.setDescription('outbound network interface address')
wfBootpRelayFwdPassThroughMode = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("bootp", 1), ("bootp-dhcp", 2), ("dhcp", 3))).clone('bootp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBootpRelayFwdPassThroughMode.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayFwdPassThroughMode.setDescription('The PROPAGATION mode for this interface: Bootp Requests only, both Bootp Requests and Bootp Requests containing DHCP messages, or Bootp Requests containing DHCP messages only.')
wfBootpRelayFwdOutReqPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpRelayFwdOutReqPkts.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayFwdOutReqPkts.setDescription('The total number of BOOTPREQUEST packets relayed out of this forwarding entry.')
wfBootpClientIntfTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 1, 1), )
if mibBuilder.loadTexts: wfBootpClientIntfTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpClientIntfTable.setDescription('for a BOOTP relay agent on a given interface, this table contains the list of DLCI-IP address assignments.')
wfBootpClientIntfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 1, 1, 1), ).setIndexNames((0, "Wellfleet-BOOTP-MIB", "wfBootpClientIntfAddress"), (0, "Wellfleet-BOOTP-MIB", "wfBootpClientIntfDlci"))
if mibBuilder.loadTexts: wfBootpClientIntfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpClientIntfEntry.setDescription('a BOOTP client interface description')
wfBootpClientIntfDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBootpClientIntfDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpClientIntfDelete.setDescription('Flag to indicate BOOTP client interface instance deletion')
wfBootpClientIntfDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpClientIntfDlci.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpClientIntfDlci.setDescription('The DLCI for the virtual circuit used by this BOOTP client')
wfBootpClientIntfAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 1, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpClientIntfAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpClientIntfAddress.setDescription('The IP address for the interface used by this BOOTP client')
wfBootpRelayPrefServTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 3), )
if mibBuilder.loadTexts: wfBootpRelayPrefServTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayPrefServTable.setDescription('This table contains Preferred Server configuration information for configured Bootp Relay Agents.')
wfBootpRelayPrefServEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 3, 1), ).setIndexNames((0, "Wellfleet-BOOTP-MIB", "wfBootpRelayPrefServAgentAddress"), (0, "Wellfleet-BOOTP-MIB", "wfBootpRelayPrefServTargetAddress"))
if mibBuilder.loadTexts: wfBootpRelayPrefServEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayPrefServEntry.setDescription('a BOOTP relay Preferred Server description')
wfBootpRelayPrefServDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBootpRelayPrefServDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayPrefServDelete.setDescription('Create/Delete: if set to delete, the static entry is removed from the table')
wfBootpRelayPrefServDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBootpRelayPrefServDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayPrefServDisable.setDescription('Enable/Disable: controls whether the static entry is included in the list of preferred servers for this interface or not.')
wfBootpRelayPrefServAgentAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpRelayPrefServAgentAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayPrefServAgentAddress.setDescription("relay agent's IP address")
wfBootpRelayPrefServTargetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 3, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpRelayPrefServTargetAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayPrefServTargetAddress.setDescription('Target Server(s) address, either unicast or multicast')
wfBootpRelayPrefServTargetName = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 3, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBootpRelayPrefServTargetName.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayPrefServTargetName.setDescription('Target Server(s) host name')
wfBootpRelayPrefServRequestMode = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("bootp", 1), ("bootp-dhcp", 2), ("dhcp", 3))).clone('bootp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBootpRelayPrefServRequestMode.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayPrefServRequestMode.setDescription('The PROPAGATION mode for this preferred server: Bootp Requests only, both Bootp Requests and Bootp Requests containing DHCP messages, or Bootp Requests containing DHCP messages only.')
wfBootpRelayPrefServOutReqPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBootpRelayPrefServOutReqPkts.setStatus('mandatory')
if mibBuilder.loadTexts: wfBootpRelayPrefServOutReqPkts.setDescription('The total number of BOOTPREQUEST packets relayed to this preferred server.')
mibBuilder.exportSymbols("Wellfleet-BOOTP-MIB", wfBootpRelayFwdDelete=wfBootpRelayFwdDelete, wfBootpRelayIntfState=wfBootpRelayIntfState, wfBootpClientIntfAddress=wfBootpClientIntfAddress, wfBootpRelayIntfPassThroughMode=wfBootpRelayIntfPassThroughMode, wfBootpRelayIntfFltrDrops=wfBootpRelayIntfFltrDrops, wfBootpRelayPrefServTargetName=wfBootpRelayPrefServTargetName, wfBootpRelayIntfReplies=wfBootpRelayIntfReplies, wfBootpClientGroup=wfBootpClientGroup, wfBootpRelayIntfResrcDrops=wfBootpRelayIntfResrcDrops, wfBootpRelayIntfHops=wfBootpRelayIntfHops, wfBootpRelayIntfDisable=wfBootpRelayIntfDisable, wfBootpRelayFwdAgentIntf=wfBootpRelayFwdAgentIntf, wfBootpRelayIntfTranReqs=wfBootpRelayIntfTranReqs, wfBootpClientIntfDlci=wfBootpClientIntfDlci, wfBootpRelayIntfSeconds=wfBootpRelayIntfSeconds, wfBootpRelayPrefServOutReqPkts=wfBootpRelayPrefServOutReqPkts, wfBootpRelayPrefServTargetAddress=wfBootpRelayPrefServTargetAddress, wfBootpRelayIntfDhcpSvDnDrps=wfBootpRelayIntfDhcpSvDnDrps, wfBootpRelayIntfDelete=wfBootpRelayIntfDelete, wfBootpRelayFwdDisable=wfBootpRelayFwdDisable, wfBootpRelayAgentGroup=wfBootpRelayAgentGroup, wfBootpRelayIntfUdpSktDrops=wfBootpRelayIntfUdpSktDrops, wfBootpServerGroup=wfBootpServerGroup, wfBootpRelayIntfTable=wfBootpRelayIntfTable, wfBootpRelayIntfArpCache=wfBootpRelayIntfArpCache, wfBootpRelayFwdEntry=wfBootpRelayFwdEntry, wfBootpRelayPrefServTable=wfBootpRelayPrefServTable, wfBootpRelayIntfRequests=wfBootpRelayIntfRequests, wfBootpRelayIntfBufLimit=wfBootpRelayIntfBufLimit, wfBootpRelayPrefServAgentAddress=wfBootpRelayPrefServAgentAddress, wfBootpRelayIntfTooShortDrops=wfBootpRelayIntfTooShortDrops, wfBootpRelayIntfSecDrops=wfBootpRelayIntfSecDrops, wfBootpRelayFwdTable=wfBootpRelayFwdTable, wfBootpRelayIntfPri=wfBootpRelayIntfPri, wfBootpRelayPrefServEntry=wfBootpRelayPrefServEntry, wfBootpRelayIntfBufDrops=wfBootpRelayIntfBufDrops, wfBootpRelayIntfAddress=wfBootpRelayIntfAddress, wfBootpRelayIntfHopsDrops=wfBootpRelayIntfHopsDrops, wfBootpRelayIntfEntry=wfBootpRelayIntfEntry, wfBootpRelayFwdPassThroughMode=wfBootpRelayFwdPassThroughMode, wfBootpRelayPrefServDisable=wfBootpRelayPrefServDisable, wfBootpRelayIntfOpDrops=wfBootpRelayIntfOpDrops, wfBootpRelayIntfDhcpSvrDsbl=wfBootpRelayIntfDhcpSvrDsbl, wfBootpRelayPrefServDelete=wfBootpRelayPrefServDelete, wfBootpRelayIntfGiaddrDrops=wfBootpRelayIntfGiaddrDrops, wfBootpClientIntfEntry=wfBootpClientIntfEntry, wfBootpClientIntfDelete=wfBootpClientIntfDelete, wfBootpRelayPrefServRequestMode=wfBootpRelayPrefServRequestMode, wfBootpRelayFwdOutReqPkts=wfBootpRelayFwdOutReqPkts, wfBootpClientIntfTable=wfBootpClientIntfTable, wfBootpRelayIntfBcastDrops=wfBootpRelayIntfBcastDrops, wfBootpRelayFwdOutIntf=wfBootpRelayFwdOutIntf)