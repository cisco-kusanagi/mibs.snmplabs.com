#
# PySNMP MIB module FOUNDRY-SN-MAC-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FOUNDRY-SN-MAC-VLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:15:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, ObjectIdentity, Gauge32, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, Unsigned32, Bits, Counter32, Counter64, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Gauge32", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "Unsigned32", "Bits", "Counter32", "Counter64", "MibIdentifier", "IpAddress")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
snMacVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30))
snMacVlan.setRevisions(('2007-06-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snMacVlan.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: snMacVlan.setLastUpdated('200706250000Z')
if mibBuilder.loadTexts: snMacVlan.setOrganization('Foundry Networks, Inc')
if mibBuilder.loadTexts: snMacVlan.setContactInfo('')
if mibBuilder.loadTexts: snMacVlan.setDescription('Management Information Base module for MAC-based Vlan configuration and statistics.')
snMacVlanGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1))
snMacVlanTableObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2))
snMacVlanGlobalClearOper = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("valid", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacVlanGlobalClearOper.setStatus('current')
if mibBuilder.loadTexts: snMacVlanGlobalClearOper.setDescription('valid(0) - a SNMP-GET of this mib shows that it is valid command to use. clear(1) - represents clear operational MAC-based Vlan entry for all ports.')
snMacVlanGlobalDynConfigState = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacVlanGlobalDynConfigState.setStatus('current')
if mibBuilder.loadTexts: snMacVlanGlobalDynConfigState.setDescription('Enable/disable MAC-based VLAN dynamic activation on the global level.')
snMacVlanPortMemberTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 1), )
if mibBuilder.loadTexts: snMacVlanPortMemberTable.setStatus('current')
if mibBuilder.loadTexts: snMacVlanPortMemberTable.setDescription('MAC-based Vlan port membership table.')
snMacVlanPortMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 1, 1), ).setIndexNames((0, "FOUNDRY-SN-MAC-VLAN-MIB", "snMacVlanPortMemberVLanId"), (0, "FOUNDRY-SN-MAC-VLAN-MIB", "snMacVlanPortMemberPortId"))
if mibBuilder.loadTexts: snMacVlanPortMemberEntry.setStatus('current')
if mibBuilder.loadTexts: snMacVlanPortMemberEntry.setDescription('An entry of the MAC-based Vlan port membership table.')
snMacVlanPortMemberVLanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: snMacVlanPortMemberVLanId.setStatus('current')
if mibBuilder.loadTexts: snMacVlanPortMemberVLanId.setDescription('The VLAN identifier (VLAN ID).')
snMacVlanPortMemberPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 1, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: snMacVlanPortMemberPortId.setStatus('current')
if mibBuilder.loadTexts: snMacVlanPortMemberPortId.setDescription('The ifIndex which is a member of the MAC-based VLAN.')
snMacVlanPortMemberRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("valid", 2), ("delete", 3), ("create", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacVlanPortMemberRowStatus.setStatus('current')
if mibBuilder.loadTexts: snMacVlanPortMemberRowStatus.setDescription("This object is used to create and delete row in the table and control if they are used. The values that can be written are: delete(3)...deletes the row create(4)...creates a new row If the row exists, then a SET with value of create(4) returns error 'wrongValue'. Deleted rows go away immediately. The following values can be returned on reads: noSuch(0)...no such row other(1)....some other case valid(2)....the row exists and is valid")
snMacVlanIfTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 2), )
if mibBuilder.loadTexts: snMacVlanIfTable.setStatus('current')
if mibBuilder.loadTexts: snMacVlanIfTable.setDescription('MAC-based Vlan Interface table.')
snMacVlanIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 2, 1), ).setIndexNames((0, "FOUNDRY-SN-MAC-VLAN-MIB", "snMacVlanIfIndex"))
if mibBuilder.loadTexts: snMacVlanIfEntry.setStatus('current')
if mibBuilder.loadTexts: snMacVlanIfEntry.setDescription('An entry in the MAC-based Vlan interface table.')
snMacVlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: snMacVlanIfIndex.setStatus('current')
if mibBuilder.loadTexts: snMacVlanIfIndex.setDescription('The ifIndex which is a member of the MAC-based VLAN.')
snMacVlanIfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacVlanIfEnable.setStatus('current')
if mibBuilder.loadTexts: snMacVlanIfEnable.setDescription('The administrative status requested by management for MAC-based Vlan on this interface. The value enabled(1) indicates that MAC-based Vlan should be enabled on this interface, When disabled(2), MAC-based Vlan is disabled on this interface. Enable/disable MAC-based Vlan on this interface.')
snMacVlanIfMaxEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 32)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacVlanIfMaxEntry.setStatus('current')
if mibBuilder.loadTexts: snMacVlanIfMaxEntry.setDescription('The maximum number of allowed and denied MAC address (static and dynamic) that can be leared on an interface. The default value is 2. The value should be between 2 to 32.')
snMacVlanIfClearOper = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("valid", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacVlanIfClearOper.setStatus('current')
if mibBuilder.loadTexts: snMacVlanIfClearOper.setDescription('valid(0) - a SNMP-GET of this mib shows that it is valid command to use. clear(1) - represents clearing operational MAC-based Vlan entry for a port.')
snMacVlanIfClearConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("valid", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacVlanIfClearConfig.setStatus('current')
if mibBuilder.loadTexts: snMacVlanIfClearConfig.setDescription('valid(0) - a SNMP-GET of this mib shows that it is valid command to use. clear(1) - represents clearing configured MAC-based Vlan entry for a port.')
snMacBasedVlanTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 3), )
if mibBuilder.loadTexts: snMacBasedVlanTable.setStatus('current')
if mibBuilder.loadTexts: snMacBasedVlanTable.setDescription('MAC-based Vlan table.')
snMacBasedVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 3, 1), ).setIndexNames((0, "FOUNDRY-SN-MAC-VLAN-MIB", "snMacVlanIfIndex"), (0, "FOUNDRY-SN-MAC-VLAN-MIB", "snMacBasedVlanId"), (0, "FOUNDRY-SN-MAC-VLAN-MIB", "snMacBasedVlanMac"))
if mibBuilder.loadTexts: snMacBasedVlanEntry.setStatus('current')
if mibBuilder.loadTexts: snMacBasedVlanEntry.setDescription('An entry in the MAC-based Vlan table.')
snMacBasedVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: snMacBasedVlanId.setStatus('current')
if mibBuilder.loadTexts: snMacBasedVlanId.setDescription('The ID of a VLAN of which this port is a mac-vlan-permit member. Port must be untagged. This object return 0 which is an invalid VLAN ID value.')
snMacBasedVlanMac = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 3, 1, 2), MacAddress())
if mibBuilder.loadTexts: snMacBasedVlanMac.setStatus('current')
if mibBuilder.loadTexts: snMacBasedVlanMac.setDescription('A host source MAC address to be authenticated.')
snMacBasedVlanPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacBasedVlanPriority.setStatus('current')
if mibBuilder.loadTexts: snMacBasedVlanPriority.setDescription('The priority of the source MAC address.')
snMacBasedVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("valid", 2), ("delete", 3), ("create", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacBasedVlanRowStatus.setStatus('current')
if mibBuilder.loadTexts: snMacBasedVlanRowStatus.setDescription("This object is used to create and delete row in the table and control if they are used. The values that can be written are: delete(3)...deletes the row create(4)...creates a new row If the row exists, then a SET with value of create(4) returns error 'wrongValue'. Deleted rows go away immediately. The following values can be returned on reads: noSuchName...no such row other(1).....some other cases valid(2)....the row exists and is valid")
mibBuilder.exportSymbols("FOUNDRY-SN-MAC-VLAN-MIB", snMacBasedVlanRowStatus=snMacBasedVlanRowStatus, snMacBasedVlanTable=snMacBasedVlanTable, snMacVlanIfEnable=snMacVlanIfEnable, snMacVlanGlobalObjects=snMacVlanGlobalObjects, snMacVlanIfEntry=snMacVlanIfEntry, snMacVlanIfTable=snMacVlanIfTable, snMacVlanPortMemberVLanId=snMacVlanPortMemberVLanId, snMacVlan=snMacVlan, snMacVlanPortMemberEntry=snMacVlanPortMemberEntry, snMacVlanIfClearOper=snMacVlanIfClearOper, snMacVlanIfIndex=snMacVlanIfIndex, snMacVlanGlobalClearOper=snMacVlanGlobalClearOper, snMacVlanIfMaxEntry=snMacVlanIfMaxEntry, snMacBasedVlanPriority=snMacBasedVlanPriority, PYSNMP_MODULE_ID=snMacVlan, snMacBasedVlanMac=snMacBasedVlanMac, snMacBasedVlanEntry=snMacBasedVlanEntry, snMacVlanPortMemberRowStatus=snMacVlanPortMemberRowStatus, snMacVlanIfClearConfig=snMacVlanIfClearConfig, snMacVlanTableObjects=snMacVlanTableObjects, snMacVlanGlobalDynConfigState=snMacVlanGlobalDynConfigState, snMacBasedVlanId=snMacBasedVlanId, snMacVlanPortMemberPortId=snMacVlanPortMemberPortId, snMacVlanPortMemberTable=snMacVlanPortMemberTable)
