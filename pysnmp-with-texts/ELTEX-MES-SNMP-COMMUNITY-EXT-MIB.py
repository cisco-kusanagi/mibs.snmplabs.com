#
# PySNMP MIB module ELTEX-MES-SNMP-COMMUNITY-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-SNMP-COMMUNITY-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:01:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
eltMesSnmpCommExtMIB, = mibBuilder.importSymbols("ELTEX-MES-MNG-MIB", "eltMesSnmpCommExtMIB")
snmpCommunityEntry, = mibBuilder.importSymbols("SNMP-COMMUNITY-MIB", "snmpCommunityEntry")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ObjectIdentity, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Unsigned32, iso, Gauge32, IpAddress, Integer32, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Unsigned32", "iso", "Gauge32", "IpAddress", "Integer32", "ModuleIdentity", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eltSnmpCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 4, 1), )
if mibBuilder.loadTexts: eltSnmpCommunityTable.setStatus('current')
if mibBuilder.loadTexts: eltSnmpCommunityTable.setDescription("The table of community strings configured in the SNMP engine's Local Configuration Datastore (LCD).")
eltSnmpCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 4, 1, 1), )
snmpCommunityEntry.registerAugmentions(("ELTEX-MES-SNMP-COMMUNITY-EXT-MIB", "eltSnmpCommunityEntry"))
eltSnmpCommunityEntry.setIndexNames(*snmpCommunityEntry.getIndexNames())
if mibBuilder.loadTexts: eltSnmpCommunityEntry.setStatus('current')
if mibBuilder.loadTexts: eltSnmpCommunityEntry.setDescription('Information about a particular community string.')
eltSnmpCommunityAccessList = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 4, 1, 1, 1), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eltSnmpCommunityAccessList.setStatus('current')
if mibBuilder.loadTexts: eltSnmpCommunityAccessList.setDescription('Index assigned to the ACL for SNMP community to filter SNMP requests.')
mibBuilder.exportSymbols("ELTEX-MES-SNMP-COMMUNITY-EXT-MIB", eltSnmpCommunityTable=eltSnmpCommunityTable, eltSnmpCommunityEntry=eltSnmpCommunityEntry, eltSnmpCommunityAccessList=eltSnmpCommunityAccessList)
