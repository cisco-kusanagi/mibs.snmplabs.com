#
# PySNMP MIB module PDN-MGMT-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-MGMT-IP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:39:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
AtmVpIdentifier, AtmVcIdentifier = mibBuilder.importSymbols("ATM-TC-MIB", "AtmVpIdentifier", "AtmVcIdentifier")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
pdn_interfaces, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-interfaces")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, Counter32, TimeTicks, MibIdentifier, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Integer32, ModuleIdentity, Bits, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "TimeTicks", "MibIdentifier", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Integer32", "ModuleIdentity", "Bits", "IpAddress", "Gauge32")
DisplayString, TextualConvention, RowStatus, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "PhysAddress")
pdnMgmtIpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21))
if mibBuilder.loadTexts: pdnMgmtIpMIB.setLastUpdated('200206051500Z')
if mibBuilder.loadTexts: pdnMgmtIpMIB.setOrganization('Paradyne Corporation MIB Working Group')
if mibBuilder.loadTexts: pdnMgmtIpMIB.setContactInfo(' Paradyne Networks Inc. Postal: 8545, 126th Ave. N. Largo, FL 33779 US Editors: Daniel M.V. Jesus Pinto Email: mibwg_team@eng.paradyne.com')
if mibBuilder.loadTexts: pdnMgmtIpMIB.setDescription('The MIB module for configuration and management of IP interfaces/ports used for managing a DSLAM.')
pdnMgmtIpConfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1))
pdnMgmtIpPortTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1), )
if mibBuilder.loadTexts: pdnMgmtIpPortTable.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtIpPortTable.setDescription('This table contains one row per IP port in the system.')
pdnMgmtIpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1, 1), ).setIndexNames((0, "PDN-MGMT-IP-MIB", "pdnMgmtIpPortIndex"))
if mibBuilder.loadTexts: pdnMgmtIpPortEntry.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtIpPortEntry.setDescription('Configuration information about a particular IP port in the system.')
pdnMgmtIpPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: pdnMgmtIpPortIndex.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtIpPortIndex.setDescription('The index for this entry.')
pdnMgmtIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnMgmtIpAddress.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtIpAddress.setDescription("The IP address assigned to this port. If the pdnMgmtIpConfigMode is set to modes other than 'manual', then the MAX-ACCESS for this object is read-only and the value of the object represents the actual IP address assigned to the port by the DHCP or BOOTP client (or 0.0.0.0, if none assigned). A 0.0.0.0 for this object indicates that no IP address is assigned to the port. Changes to this object could disrupt data flow through the port as the IP port tears down the IP stack first before instantiating the stack again with the new IP address.")
pdnMgmtIpNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnMgmtIpNetMask.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtIpNetMask.setDescription("The IP subnet mask assigned to this port. If the pdnMgmtIpConfigMode is set to modes other than 'manual', then the MAX-ACCESS for this object is read-only and the value of the object represents the actual IP subnet mask assigned to the port by the DHCP or BOOTP client (or 0.0.0.0, if none assigned). A 0.0.0.0 for the this object indicates that no IP subnet mask is assigned to the port. Changes to this object could disrupt data flow through the port as the IP port tears down the IP stack first before instantiating the stack again with the new IP subnet mask.")
pdnMgmtIpEthGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnMgmtIpEthGateway.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtIpEthGateway.setDescription("The IP Gateway for an ethernet based IP port. This object is supported only on IP ports that are configured to run over ethernet type of media. This object would be set to 0.0.0.0 for other types of interfaces and is not valid. Furthermore, if the pdnMgmtIpConfigMode is set to modes other than 'manual', then the MAX-ACCESS for this object is read-only and the value of the object represents the actual IP Gateway mask assigned to the port by the DHCP or BOOTP client (or 0.0.0.0, if none assigned). A 0.0.0.0 for this object indicates that no IP Gateway is assigned to the port.")
pdnMgmtIpPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1, 1, 5), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnMgmtIpPhysAddress.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtIpPhysAddress.setDescription('The physical address associated with the media. For IP Ports with Ethernet type of media, the MAX-ACCESS for this object is restricted to read-only. In such cases, this object would reflect the MAC address of the underlying ethernet data link. For IP Ports that run over ATM PVCs, this object is writable.')
pdnMgmtIpConfigMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("manual", 1), ("dhcp", 2), ("bootp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnMgmtIpConfigMode.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtIpConfigMode.setDescription("The IP configuration mode for the port. In 'manual' mode, it is upto the user to provide the IP address &amp; IP subnet mask of the port. In 'dhcp' or 'bootp' modes, the respective protocols are resposible to obtain and populate the IP address &amp; IP subnet mask for the port. Whenever the config mode is changed from 'manual' mode, the IP address and the IP subnet mask for the port would automatically be reset to 0.0.0.0. The external agent (SNMP or others) SHOULD NOT attempt to write the IP address or the IP subnet mask of the port when this object is not in 'manual' mode.")
pdnMgmtBootIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1, 1, 7), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnMgmtBootIfIndex.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtBootIfIndex.setDescription("The interface index of the ATM interface to be used by BOOTP or DHCP client, if the pdnMgmtIpConfigMode is set to 'bootp' or 'dhcp' respectively. Even if the IP port (interface) is configured for 'manual' configuration, the value of this object can be modified to indicate the default ATM ifIndex for BOOTP or DHCP to operate on. This object is valid only if the IP Port has ATM PVC(s) as the underlying data link media. For IP Ports over ethernet type of media, the MAX-ACCESS for this object is read-only, and the object is set to 0 always.")
pdnMgmtBootVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1, 1, 8), AtmVpIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnMgmtBootVpi.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtBootVpi.setDescription("The VPI of the ATM PVC to be used by BOOTP or DHCP client, if the pdnMgmtIpConfigMode is set to 'bootp' or 'dhcp' respectively. Even if the IP port (interface) is configured for 'manual' configuration, the value of this object can be modified to indicate the default ATM PVC's VPI for BOOTP or DHCP to operate on. This object is valid only if the IP Port has ATM PVC(s) as the underlying data link media. For IP Ports over ethernet type of media, the MAX-ACCESS for this object is read-only, and the object is set to 0 always.")
pdnMgmtBootVci = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1, 1, 9), AtmVcIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnMgmtBootVci.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtBootVci.setDescription("The VCI of the ATM PVC to be used by BOOTP or DHCP client, if the pdnMgmtIpConfigMode is set to 'bootp' or 'dhcp' respectively. Even if the IP port (interface) is configured for 'manual' configuration, the value of this object can be modified to indicate the default ATM PVC's VCI for BOOTP or DHCP to operate on. This object is valid only if the IP Port has ATM PVC(s) as the underlying data link media. For IP Ports over ethernet type of media, the MAX-ACCESS for this object is read-only, and the object is set to 0 always.")
pdnMgmtIpAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnMgmtIpAdminStatus.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtIpAdminStatus.setDescription("The status of the IP Port (interface). Data flow through the IP Port is possible only if this object is set to 'up'. When this object is set to 'down', the interface SHALL be torn down and all routes (associated with this port) be purged automatically, until the port is set to 'up' state again.")
pdnMgmtAtmInvArpTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 2), )
if mibBuilder.loadTexts: pdnMgmtAtmInvArpTable.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtAtmInvArpTable.setDescription('This table contains one row per Inverse ATM ARP entry in the system. This table maps the &lt;ifIndex, vpi, vci&gt; index to corresponding &lt;ipPortIndex, remoteIp&gt;.')
pdnMgmtAtmInvArpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 2, 1), ).setIndexNames((0, "PDN-MGMT-IP-MIB", "pdnMgmtAtmIfIndex"), (0, "PDN-MGMT-IP-MIB", "pdnMgmtAtmVpi"), (0, "PDN-MGMT-IP-MIB", "pdnMgmtAtmVci"))
if mibBuilder.loadTexts: pdnMgmtAtmInvArpEntry.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtAtmInvArpEntry.setDescription('ATM Inverse ARP entry corresponding to a particular ATM PVC that is being used by management IP traffic.')
pdnMgmtAtmIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: pdnMgmtAtmIfIndex.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtAtmIfIndex.setDescription('The interface index associated with the ATM PVC.')
pdnMgmtAtmVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 2, 1, 2), AtmVpIdentifier())
if mibBuilder.loadTexts: pdnMgmtAtmVpi.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtAtmVpi.setDescription('The VPI associated with the ATM PVC.')
pdnMgmtAtmVci = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 2, 1, 3), AtmVcIdentifier())
if mibBuilder.loadTexts: pdnMgmtAtmVci.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtAtmVci.setDescription('The VCI associated with the ATM PVC.')
pdnMgmtIpPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 2, 1, 4), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnMgmtIpPortIfIndex.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtIpPortIfIndex.setDescription('The Interface Index of the IP port to which this inverse ARP entry is associated with.')
pdnMgmtNextHopIp = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 2, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnMgmtNextHopIp.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtNextHopIp.setDescription('The IP address of the unit at the other end of this ATM PVC. This represents the IP Gateway equivalent for IP traffic on this specific ATM PVC.')
pdnMgmtAtmInvArpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnMgmtAtmInvArpRowStatus.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtAtmInvArpRowStatus.setDescription('This object is used to create/delete the ATM inverse ARP entry in this table. ')
pdnMgmtIpDefaultRouter = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnMgmtIpDefaultRouter.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtIpDefaultRouter.setDescription('This object identifies the default IP router to use for IP packets with no other known route. An IP address of 0.0.0.0 would disable and delete the default route from the system.')
pdnMgmtIpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 2))
pdnMgmtIpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 2, 1))
pdnMgmtIpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 2, 2))
pdnMgmtIpConfigCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 2, 2, 1)).setObjects(("PDN-MGMT-IP-MIB", "pdnMgmtIpConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnMgmtIpConfigCompliance = pdnMgmtIpConfigCompliance.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtIpConfigCompliance.setDescription('The compliance statement for SNMP entities which manage the configuration parameters on a Management IP port/interface.')
pdnMgmtIpConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 2, 1, 1)).setObjects(("PDN-MGMT-IP-MIB", "pdnMgmtIpAddress"), ("PDN-MGMT-IP-MIB", "pdnMgmtIpNetMask"), ("PDN-MGMT-IP-MIB", "pdnMgmtIpEthGateway"), ("PDN-MGMT-IP-MIB", "pdnMgmtIpPhysAddress"), ("PDN-MGMT-IP-MIB", "pdnMgmtIpConfigMode"), ("PDN-MGMT-IP-MIB", "pdnMgmtBootIfIndex"), ("PDN-MGMT-IP-MIB", "pdnMgmtBootVpi"), ("PDN-MGMT-IP-MIB", "pdnMgmtBootVci"), ("PDN-MGMT-IP-MIB", "pdnMgmtIpAdminStatus"), ("PDN-MGMT-IP-MIB", "pdnMgmtIpPortIfIndex"), ("PDN-MGMT-IP-MIB", "pdnMgmtNextHopIp"), ("PDN-MGMT-IP-MIB", "pdnMgmtAtmInvArpRowStatus"), ("PDN-MGMT-IP-MIB", "pdnMgmtIpDefaultRouter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnMgmtIpConfigGroup = pdnMgmtIpConfigGroup.setStatus('current')
if mibBuilder.loadTexts: pdnMgmtIpConfigGroup.setDescription('A collection of Management IP configuration objects that are required to configure the device.')
mibBuilder.exportSymbols("PDN-MGMT-IP-MIB", pdnMgmtAtmVci=pdnMgmtAtmVci, pdnMgmtAtmInvArpRowStatus=pdnMgmtAtmInvArpRowStatus, pdnMgmtIpConformance=pdnMgmtIpConformance, pdnMgmtIpPortTable=pdnMgmtIpPortTable, pdnMgmtIpPortEntry=pdnMgmtIpPortEntry, pdnMgmtIpNetMask=pdnMgmtIpNetMask, pdnMgmtBootVci=pdnMgmtBootVci, pdnMgmtIpMIB=pdnMgmtIpMIB, pdnMgmtNextHopIp=pdnMgmtNextHopIp, pdnMgmtIpAdminStatus=pdnMgmtIpAdminStatus, pdnMgmtAtmInvArpTable=pdnMgmtAtmInvArpTable, pdnMgmtIpDefaultRouter=pdnMgmtIpDefaultRouter, pdnMgmtIpPortIndex=pdnMgmtIpPortIndex, pdnMgmtIpConfObjects=pdnMgmtIpConfObjects, pdnMgmtAtmIfIndex=pdnMgmtAtmIfIndex, pdnMgmtAtmInvArpEntry=pdnMgmtAtmInvArpEntry, pdnMgmtAtmVpi=pdnMgmtAtmVpi, pdnMgmtBootIfIndex=pdnMgmtBootIfIndex, pdnMgmtIpGroups=pdnMgmtIpGroups, pdnMgmtIpPortIfIndex=pdnMgmtIpPortIfIndex, pdnMgmtIpConfigGroup=pdnMgmtIpConfigGroup, pdnMgmtBootVpi=pdnMgmtBootVpi, pdnMgmtIpCompliances=pdnMgmtIpCompliances, pdnMgmtIpPhysAddress=pdnMgmtIpPhysAddress, pdnMgmtIpConfigCompliance=pdnMgmtIpConfigCompliance, pdnMgmtIpConfigMode=pdnMgmtIpConfigMode, pdnMgmtIpAddress=pdnMgmtIpAddress, PYSNMP_MODULE_ID=pdnMgmtIpMIB, pdnMgmtIpEthGateway=pdnMgmtIpEthGateway)
