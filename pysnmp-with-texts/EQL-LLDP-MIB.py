#
# PySNMP MIB module EQL-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EQL-LLDP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:05:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
eqlGroupId, = mibBuilder.importSymbols("EQLGROUP-MIB", "eqlGroupId")
eqlMemberIndex, = mibBuilder.importSymbols("EQLMEMBER-MIB", "eqlMemberIndex")
equalLogic, = mibBuilder.importSymbols("EQUALLOGIC-SMI", "equalLogic")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, ModuleIdentity, Unsigned32, IpAddress, MibIdentifier, Counter32, iso, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, NotificationType, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ModuleIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "Counter32", "iso", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "NotificationType", "Integer32", "Bits")
TruthValue, TimeInterval, MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeInterval", "MacAddress", "DisplayString", "TextualConvention")
eqlLldpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740, 21))
eqlLldpMib.setRevisions(('2010-07-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eqlLldpMib.setRevisionsDescriptions(('Initial revision - based on IEEE 802.1AB-2009 Copyright (C) IEEE.',))
if mibBuilder.loadTexts: eqlLldpMib.setLastUpdated('201403121459Z')
if mibBuilder.loadTexts: eqlLldpMib.setOrganization('EqualLogic Inc.')
if mibBuilder.loadTexts: eqlLldpMib.setContactInfo('Contact: Customer Support Postal: Dell Inc 300 Innovative Way, Suite 301, Nashua, NH 03062 Tel: +1 603-579-9762 E-mail: US-NH-CS-TechnicalSupport@dell.com WEB: www.equallogic.com')
if mibBuilder.loadTexts: eqlLldpMib.setDescription('Link Layer Discovery Protocol MIB module. Copyright (c) 2010-2012 by Dell Inc. All rights reserved. This software may not be copied, disclosed, transferred, or used except in accordance with a license granted by Dell Inc. This software embodies proprietary information and trade secrets of Dell Inc. Copyright (C) IEEE (2009). This version of this MIB module is published as subclause 11.5.1 of IEEE Std 802.1AB-2009; see the standard itself for full legal notices.')
eqlLldpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 21, 1))
class EqlLldpV2ChassisIdSubtype(TextualConvention, Integer32):
    description = 'This describes the source of a chassis identifier.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("chassisComponent", 1), ("interfaceAlias", 2), ("portComponent", 3), ("macAddress", 4), ("networkAddress", 5), ("interfaceName", 6), ("local", 7))

class EqlLldpV2ChassisId(TextualConvention, OctetString):
    description = 'This describes the format of a chassis identifier string.'
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(255, 255)
    fixedLength = 255

class EqlLldpV2PortIdSubtype(TextualConvention, Integer32):
    description = 'This describes the source of a particular type of port identifier used in the LLDP MIB.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("interfaceAlias", 1), ("portComponent", 2), ("macAddress", 3), ("networkAddress", 4), ("interfaceName", 5), ("agentCircuitId", 6), ("local", 7))

class EqlLldpV2PortId(TextualConvention, OctetString):
    description = 'This describes the format of a port identifier string.'
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class EqlLldpV2State(TextualConvention, Integer32):
    description = 'This describes the state of LLDP for the port.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("off", 0), ("noPeer", 1), ("active", 2), ("multiplePeers", 3))

eqlLldpDynamicIfTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1), )
if mibBuilder.loadTexts: eqlLldpDynamicIfTable.setStatus('current')
if mibBuilder.loadTexts: eqlLldpDynamicIfTable.setDescription("EqualLogic-Dynamic A table of LLDP information per each interface of a system. Each row in this table supplies values for one port's LLDP parameters.")
eqlLldpDynamicIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: eqlLldpDynamicIfEntry.setStatus('current')
if mibBuilder.loadTexts: eqlLldpDynamicIfEntry.setDescription('An entry in the LLDP table, containing information about LLDP on a single interface.')
eqlLldpRemMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpRemMacAddress.setStatus('current')
if mibBuilder.loadTexts: eqlLldpRemMacAddress.setDescription('The MAC address associated with the LLDP peer.')
eqlLldpV2RemChassisIdSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 2), EqlLldpV2ChassisIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemChassisIdSubtype.setStatus('current')
if mibBuilder.loadTexts: eqlLldpV2RemChassisIdSubtype.setDescription('The type of encoding used to identify the chassis associated with the remote system.')
eqlLldpV2RemChassisId = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 3), EqlLldpV2ChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemChassisId.setStatus('current')
if mibBuilder.loadTexts: eqlLldpV2RemChassisId.setDescription('The string value used to identify the chassis component associated with the remote system.')
eqlLldpV2RemPortIdSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 4), EqlLldpV2PortIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemPortIdSubtype.setStatus('current')
if mibBuilder.loadTexts: eqlLldpV2RemPortIdSubtype.setDescription('The type of encoding used to identify the port associated with the remote system.')
eqlLldpV2RemPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 5), EqlLldpV2PortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemPortId.setStatus('current')
if mibBuilder.loadTexts: eqlLldpV2RemPortId.setDescription('The string value used to identify the port component associated with the remote system.')
eqlLldpV2RemPortDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemPortDesc.setStatus('current')
if mibBuilder.loadTexts: eqlLldpV2RemPortDesc.setDescription('The string value used to identify the description of the given port associated with the remote system.')
eqlLldpV2RemSysName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemSysName.setStatus('current')
if mibBuilder.loadTexts: eqlLldpV2RemSysName.setDescription('The string value used to identify the system name of the remote system.')
eqlLldpV2RemSysDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemSysDesc.setStatus('current')
if mibBuilder.loadTexts: eqlLldpV2RemSysDesc.setDescription('The string value used to identify the system description of the remote system.')
eqlLldpV2State = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 9), EqlLldpV2State()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2State.setStatus('current')
if mibBuilder.loadTexts: eqlLldpV2State.setDescription('The current LLDP state for the port.')
eqlLldpV2RemMgmtAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemMgmtAddr.setStatus('current')
if mibBuilder.loadTexts: eqlLldpV2RemMgmtAddr.setDescription('The management address reported by the remote system. If multiple addresses were reported, they are delimited by commas.')
mibBuilder.exportSymbols("EQL-LLDP-MIB", eqlLldpDynamicIfTable=eqlLldpDynamicIfTable, eqlLldpV2RemPortId=eqlLldpV2RemPortId, eqlLldpV2RemPortDesc=eqlLldpV2RemPortDesc, eqlLldpV2RemChassisId=eqlLldpV2RemChassisId, eqlLldpV2State=eqlLldpV2State, EqlLldpV2State=EqlLldpV2State, EqlLldpV2PortId=EqlLldpV2PortId, eqlLldpV2RemSysName=eqlLldpV2RemSysName, eqlLldpV2RemMgmtAddr=eqlLldpV2RemMgmtAddr, PYSNMP_MODULE_ID=eqlLldpMib, eqlLldpV2RemPortIdSubtype=eqlLldpV2RemPortIdSubtype, eqlLldpRemMacAddress=eqlLldpRemMacAddress, eqlLldpV2RemSysDesc=eqlLldpV2RemSysDesc, eqlLldpDynamicIfEntry=eqlLldpDynamicIfEntry, eqlLldpMIBObjects=eqlLldpMIBObjects, EqlLldpV2PortIdSubtype=EqlLldpV2PortIdSubtype, eqlLldpV2RemChassisIdSubtype=eqlLldpV2RemChassisIdSubtype, eqlLldpMib=eqlLldpMib, EqlLldpV2ChassisId=EqlLldpV2ChassisId, EqlLldpV2ChassisIdSubtype=EqlLldpV2ChassisIdSubtype)
