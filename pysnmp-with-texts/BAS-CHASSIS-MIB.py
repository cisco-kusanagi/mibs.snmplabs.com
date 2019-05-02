#
# PySNMP MIB module BAS-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAS-CHASSIS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:33:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
BasChassisId, BasSlotId, BasLogicalPortId, BasCardClass, basChassisInfo, BasInterfaceId = mibBuilder.importSymbols("BAS-MIB", "BasChassisId", "BasSlotId", "BasLogicalPortId", "BasCardClass", "basChassisInfo", "BasInterfaceId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Bits, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, NotificationType, Gauge32, IpAddress, MibIdentifier, Counter64, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "NotificationType", "Gauge32", "IpAddress", "MibIdentifier", "Counter64", "Unsigned32", "ObjectIdentity")
DateAndTime, TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
basChassisInfoMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1))
if mibBuilder.loadTexts: basChassisInfoMib.setLastUpdated('9901180900Z')
if mibBuilder.loadTexts: basChassisInfoMib.setOrganization('Broadband Access Systems')
if mibBuilder.loadTexts: basChassisInfoMib.setContactInfo(' Tech Support Broadband Access Systems 201 Forest Street Marlboro, MA 01752 U.S.A. 508-485-8200 support@basystems.com')
if mibBuilder.loadTexts: basChassisInfoMib.setDescription('This MIB module defines the Chassis Mib for a Broadband Access System Chassis cards.')
basChassisObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1))
basChassisDhcpRelayObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 2))
basChassisInfoTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1), )
if mibBuilder.loadTexts: basChassisInfoTable.setStatus('current')
if mibBuilder.loadTexts: basChassisInfoTable.setDescription('Info about this slot.')
basChassisInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1), ).setIndexNames((0, "BAS-CHASSIS-MIB", "basChassisInfoChassis"), (0, "BAS-CHASSIS-MIB", "basChassisInfoSlot"), (0, "BAS-CHASSIS-MIB", "basChassisInfoIf"), (0, "BAS-CHASSIS-MIB", "basChassisInfoLPort"))
if mibBuilder.loadTexts: basChassisInfoEntry.setStatus('current')
if mibBuilder.loadTexts: basChassisInfoEntry.setDescription('Chassis and slot and Agent information.')
basChassisInfoChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 1), BasChassisId())
if mibBuilder.loadTexts: basChassisInfoChassis.setStatus('current')
if mibBuilder.loadTexts: basChassisInfoChassis.setDescription('The BAS Chassis ID of this card.')
basChassisInfoSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 2), BasSlotId())
if mibBuilder.loadTexts: basChassisInfoSlot.setStatus('current')
if mibBuilder.loadTexts: basChassisInfoSlot.setDescription('The BAS Slot ID of this card.')
basChassisInfoIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 3), BasInterfaceId())
if mibBuilder.loadTexts: basChassisInfoIf.setStatus('current')
if mibBuilder.loadTexts: basChassisInfoIf.setDescription('The BAS interface ID of this card.')
basChassisInfoLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 4), BasLogicalPortId())
if mibBuilder.loadTexts: basChassisInfoLPort.setStatus('current')
if mibBuilder.loadTexts: basChassisInfoLPort.setDescription('The BAS logical port ID of this card.')
basChassisInfoChassisId = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 5), BasChassisId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basChassisInfoChassisId.setStatus('current')
if mibBuilder.loadTexts: basChassisInfoChassisId.setDescription('The BAS Chassis ID.')
basChassisInfoClusterId = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basChassisInfoClusterId.setStatus('current')
if mibBuilder.loadTexts: basChassisInfoClusterId.setDescription('The BAS Chassis ID.')
basChassisInfoLdapServerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basChassisInfoLdapServerIpAddr.setStatus('current')
if mibBuilder.loadTexts: basChassisInfoLdapServerIpAddr.setDescription('The LDAP Server IP Address Object')
basChassisInfoLdapServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basChassisInfoLdapServerPort.setStatus('current')
if mibBuilder.loadTexts: basChassisInfoLdapServerPort.setDescription('The LDAP Server Port Object')
basChassisInfoLdapServerUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basChassisInfoLdapServerUserName.setStatus('current')
if mibBuilder.loadTexts: basChassisInfoLdapServerUserName.setDescription('The LDAP Server username Object')
basChassisInfoLdapServerPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basChassisInfoLdapServerPassword.setStatus('current')
if mibBuilder.loadTexts: basChassisInfoLdapServerPassword.setDescription('The LDAP Server Password Object')
basChassisInfoLdapServerEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basChassisInfoLdapServerEnable.setStatus('current')
if mibBuilder.loadTexts: basChassisInfoLdapServerEnable.setDescription('The LDAP Server status Object')
basChassisIsProvisioningServer = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 12), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basChassisIsProvisioningServer.setStatus('current')
if mibBuilder.loadTexts: basChassisIsProvisioningServer.setDescription('Indicates whether the Provisioning Server is enabled or not.')
basChassisIsProvServerOnThisChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 13), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basChassisIsProvServerOnThisChassis.setStatus('current')
if mibBuilder.loadTexts: basChassisIsProvServerOnThisChassis.setDescription('Indicates whether the Provisioning Server is on this chassis or not.')
basChassisManagerTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 2), )
if mibBuilder.loadTexts: basChassisManagerTable.setStatus('current')
if mibBuilder.loadTexts: basChassisManagerTable.setDescription('Info about this slot.')
basChassisManagerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 2, 1), ).setIndexNames((0, "BAS-CHASSIS-MIB", "basChassisManagerChassis"), (0, "BAS-CHASSIS-MIB", "basChassisManagerSlot"), (0, "BAS-CHASSIS-MIB", "basChassisManagerIf"), (0, "BAS-CHASSIS-MIB", "basChassisManagerLPort"))
if mibBuilder.loadTexts: basChassisManagerEntry.setStatus('current')
if mibBuilder.loadTexts: basChassisManagerEntry.setDescription('Chassis and slot and Agent Managerrmation.')
basChassisManagerChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 2, 1, 1), BasChassisId())
if mibBuilder.loadTexts: basChassisManagerChassis.setStatus('current')
if mibBuilder.loadTexts: basChassisManagerChassis.setDescription('The BAS Chassis ID of this card.')
basChassisManagerSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 2, 1, 2), BasSlotId())
if mibBuilder.loadTexts: basChassisManagerSlot.setStatus('current')
if mibBuilder.loadTexts: basChassisManagerSlot.setDescription('The BAS Slot ID of this card.')
basChassisManagerIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 2, 1, 3), BasInterfaceId())
if mibBuilder.loadTexts: basChassisManagerIf.setStatus('current')
if mibBuilder.loadTexts: basChassisManagerIf.setDescription('The BAS interface ID of this card.')
basChassisManagerLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 2, 1, 4), BasLogicalPortId())
if mibBuilder.loadTexts: basChassisManagerLPort.setStatus('current')
if mibBuilder.loadTexts: basChassisManagerLPort.setDescription('The BAS logical port ID of this card.')
basChassisManagerAgentTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basChassisManagerAgentTcpPort.setStatus('current')
if mibBuilder.loadTexts: basChassisManagerAgentTcpPort.setDescription('The BAS Agentx Tcp Port Object')
basChassisManagerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basChassisManagerPriority.setStatus('current')
if mibBuilder.loadTexts: basChassisManagerPriority.setDescription('The BAS Chassis manager priority Object')
basChassisManagerScope = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bca", 1), ("ca", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basChassisManagerScope.setStatus('current')
if mibBuilder.loadTexts: basChassisManagerScope.setDescription('The BAS Chassis manager Object')
basChassisManagerDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 2, 1, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basChassisManagerDateAndTime.setStatus('current')
if mibBuilder.loadTexts: basChassisManagerDateAndTime.setDescription('The BCM notion of the local date and time of day.')
basChassisDhcpRelayServerTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 2, 1), )
if mibBuilder.loadTexts: basChassisDhcpRelayServerTable.setStatus('current')
if mibBuilder.loadTexts: basChassisDhcpRelayServerTable.setDescription('A list of DHCP Relay Server entries.')
basChassisDhcpRelayServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 2, 1, 1), ).setIndexNames((0, "BAS-CHASSIS-MIB", "basChassisDhcpRelayServerChassis"), (0, "BAS-CHASSIS-MIB", "basChassisDhcpRelayServerSlot"), (0, "BAS-CHASSIS-MIB", "basChassisDhcpRelayServerIf"), (0, "BAS-CHASSIS-MIB", "basChassisDhcpRelayServerLPort"), (0, "BAS-CHASSIS-MIB", "basChassisDhcpRelayServerAddress"), (0, "BAS-CHASSIS-MIB", "basChassisDhcpRelayServerType"))
if mibBuilder.loadTexts: basChassisDhcpRelayServerEntry.setStatus('current')
if mibBuilder.loadTexts: basChassisDhcpRelayServerEntry.setDescription('An entry containing management information applicable to a particular DHCP Relay Server.')
basChassisDhcpRelayServerChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 2, 1, 1, 1), BasChassisId())
if mibBuilder.loadTexts: basChassisDhcpRelayServerChassis.setStatus('current')
if mibBuilder.loadTexts: basChassisDhcpRelayServerChassis.setDescription('The BAS Chassis ID of the Card.')
basChassisDhcpRelayServerSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 2, 1, 1, 2), BasSlotId())
if mibBuilder.loadTexts: basChassisDhcpRelayServerSlot.setStatus('current')
if mibBuilder.loadTexts: basChassisDhcpRelayServerSlot.setDescription('The BAS Slot ID of the Card.')
basChassisDhcpRelayServerIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 2, 1, 1, 3), BasInterfaceId())
if mibBuilder.loadTexts: basChassisDhcpRelayServerIf.setStatus('current')
if mibBuilder.loadTexts: basChassisDhcpRelayServerIf.setDescription('The BAS interface ID of the Card.')
basChassisDhcpRelayServerLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 2, 1, 1, 4), BasLogicalPortId())
if mibBuilder.loadTexts: basChassisDhcpRelayServerLPort.setStatus('current')
if mibBuilder.loadTexts: basChassisDhcpRelayServerLPort.setDescription('The BAS logical port ID of the Card.')
basChassisDhcpRelayServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 2, 1, 1, 5), IpAddress().clone(2))
if mibBuilder.loadTexts: basChassisDhcpRelayServerAddress.setStatus('current')
if mibBuilder.loadTexts: basChassisDhcpRelayServerAddress.setDescription('Address of DHCP Relay Server on this forwarder.')
basChassisDhcpRelayServerType = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unauthorized", 1), ("authorized", 2), ("cablemodem", 3))).clone(1))
if mibBuilder.loadTexts: basChassisDhcpRelayServerType.setStatus('current')
if mibBuilder.loadTexts: basChassisDhcpRelayServerType.setDescription('Type of DHCP server. When picking a DHCP server, \\ choice is made depending on type.')
basChassisDhcpRelayServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 2, 1, 1, 7), RowStatus().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basChassisDhcpRelayServerStatus.setStatus('current')
if mibBuilder.loadTexts: basChassisDhcpRelayServerStatus.setDescription('Adding and deleting the Server.')
mibBuilder.exportSymbols("BAS-CHASSIS-MIB", basChassisDhcpRelayServerLPort=basChassisDhcpRelayServerLPort, basChassisInfoLPort=basChassisInfoLPort, basChassisManagerTable=basChassisManagerTable, basChassisObjects=basChassisObjects, basChassisIsProvServerOnThisChassis=basChassisIsProvServerOnThisChassis, basChassisInfoLdapServerUserName=basChassisInfoLdapServerUserName, basChassisManagerDateAndTime=basChassisManagerDateAndTime, basChassisInfoTable=basChassisInfoTable, basChassisInfoEntry=basChassisInfoEntry, basChassisDhcpRelayServerStatus=basChassisDhcpRelayServerStatus, basChassisDhcpRelayServerTable=basChassisDhcpRelayServerTable, basChassisManagerPriority=basChassisManagerPriority, basChassisManagerIf=basChassisManagerIf, basChassisDhcpRelayServerChassis=basChassisDhcpRelayServerChassis, basChassisDhcpRelayServerAddress=basChassisDhcpRelayServerAddress, basChassisInfoLdapServerIpAddr=basChassisInfoLdapServerIpAddr, basChassisInfoSlot=basChassisInfoSlot, PYSNMP_MODULE_ID=basChassisInfoMib, basChassisDhcpRelayObjects=basChassisDhcpRelayObjects, basChassisInfoLdapServerPort=basChassisInfoLdapServerPort, basChassisInfoLdapServerPassword=basChassisInfoLdapServerPassword, basChassisManagerSlot=basChassisManagerSlot, basChassisDhcpRelayServerSlot=basChassisDhcpRelayServerSlot, basChassisInfoChassis=basChassisInfoChassis, basChassisInfoIf=basChassisInfoIf, basChassisManagerEntry=basChassisManagerEntry, basChassisDhcpRelayServerType=basChassisDhcpRelayServerType, basChassisInfoClusterId=basChassisInfoClusterId, basChassisManagerLPort=basChassisManagerLPort, basChassisIsProvisioningServer=basChassisIsProvisioningServer, basChassisManagerAgentTcpPort=basChassisManagerAgentTcpPort, basChassisInfoMib=basChassisInfoMib, basChassisManagerChassis=basChassisManagerChassis, basChassisInfoLdapServerEnable=basChassisInfoLdapServerEnable, basChassisDhcpRelayServerIf=basChassisDhcpRelayServerIf, basChassisManagerScope=basChassisManagerScope, basChassisDhcpRelayServerEntry=basChassisDhcpRelayServerEntry, basChassisInfoChassisId=basChassisInfoChassisId)
