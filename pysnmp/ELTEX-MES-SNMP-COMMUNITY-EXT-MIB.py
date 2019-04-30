#
# PySNMP MIB module ELTEX-MES-SNMP-COMMUNITY-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-SNMP-COMMUNITY-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:47:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
eltMesSnmpCommExtMIB, = mibBuilder.importSymbols("ELTEX-MES-MNG-MIB", "eltMesSnmpCommExtMIB")
snmpCommunityEntry, = mibBuilder.importSymbols("SNMP-COMMUNITY-MIB", "snmpCommunityEntry")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, Bits, iso, ModuleIdentity, Counter64, NotificationType, TimeTicks, ObjectIdentity, Unsigned32, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "Bits", "iso", "ModuleIdentity", "Counter64", "NotificationType", "TimeTicks", "ObjectIdentity", "Unsigned32", "MibIdentifier", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eltSnmpCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 4, 1), )
if mibBuilder.loadTexts: eltSnmpCommunityTable.setStatus('current')
eltSnmpCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 4, 1, 1), )
snmpCommunityEntry.registerAugmentions(("ELTEX-MES-SNMP-COMMUNITY-EXT-MIB", "eltSnmpCommunityEntry"))
eltSnmpCommunityEntry.setIndexNames(*snmpCommunityEntry.getIndexNames())
if mibBuilder.loadTexts: eltSnmpCommunityEntry.setStatus('current')
eltSnmpCommunityAccessList = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 4, 1, 1, 1), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eltSnmpCommunityAccessList.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-SNMP-COMMUNITY-EXT-MIB", eltSnmpCommunityAccessList=eltSnmpCommunityAccessList, eltSnmpCommunityEntry=eltSnmpCommunityEntry, eltSnmpCommunityTable=eltSnmpCommunityTable)
