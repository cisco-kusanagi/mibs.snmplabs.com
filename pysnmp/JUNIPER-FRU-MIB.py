#
# PySNMP MIB module JUNIPER-FRU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-FRU-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:48:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
jnxFruMibRoot, jnxFruTraps = mibBuilder.importSymbols("JUNIPER-SMI", "jnxFruMibRoot", "jnxFruTraps")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, MibIdentifier, Counter64, IpAddress, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, ModuleIdentity, Integer32, Bits, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "Counter64", "IpAddress", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "ModuleIdentity", "Integer32", "Bits", "iso", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxFruMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 74, 1))
jnxFruMib.setRevisions(('2012-01-26 00:00',))
if mibBuilder.loadTexts: jnxFruMib.setLastUpdated('201211131414Z')
if mibBuilder.loadTexts: jnxFruMib.setOrganization('Juniper Networks, Inc.')
class JnxFruAdminStates(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("inService", 1), ("outOfService", 2))

class JnxFruOperStates(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unEquipped", 1), ("init", 2), ("normal", 3), ("mismatched", 4), ("fault", 5), ("swul", 6))

jnxFruCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1))
jnxFruCfgTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1), )
if mibBuilder.loadTexts: jnxFruCfgTable.setStatus('current')
jnxFruCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1), ).setIndexNames((0, "JUNIPER-FRU-MIB", "jnxFruCfgContentsIndex"), (0, "JUNIPER-FRU-MIB", "jnxFruCfgL1Index"), (0, "JUNIPER-FRU-MIB", "jnxFruCfgL2Index"), (0, "JUNIPER-FRU-MIB", "jnxFruCfgL3Index"))
if mibBuilder.loadTexts: jnxFruCfgEntry.setStatus('current')
jnxFruCfgContentsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxFruCfgContentsIndex.setStatus('current')
jnxFruCfgL1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxFruCfgL1Index.setStatus('current')
jnxFruCfgL2Index = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxFruCfgL2Index.setStatus('current')
jnxFruCfgL3Index = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxFruCfgL3Index.setStatus('current')
jnxFruCfgType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1, 5), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jnxFruCfgType.setStatus('current')
jnxFruCfgAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1, 6), JnxFruAdminStates()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jnxFruCfgAdminState.setStatus('current')
jnxFruCfgOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1, 7), JnxFruOperStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFruCfgOperState.setStatus('current')
jnxFruNotifMismatch = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 23, 1)).setObjects(("JUNIPER-FRU-MIB", "jnxFruCfgContentsIndex"), ("JUNIPER-FRU-MIB", "jnxFruCfgL1Index"), ("JUNIPER-FRU-MIB", "jnxFruCfgL2Index"), ("JUNIPER-FRU-MIB", "jnxFruCfgL3Index"), ("JUNIPER-FRU-MIB", "jnxFruCfgType"))
if mibBuilder.loadTexts: jnxFruNotifMismatch.setStatus('current')
jnxFruNotifAdminStatus = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 23, 2)).setObjects(("JUNIPER-FRU-MIB", "jnxFruCfgContentsIndex"), ("JUNIPER-FRU-MIB", "jnxFruCfgL1Index"), ("JUNIPER-FRU-MIB", "jnxFruCfgL2Index"), ("JUNIPER-FRU-MIB", "jnxFruCfgL3Index"), ("JUNIPER-FRU-MIB", "jnxFruCfgAdminState"))
if mibBuilder.loadTexts: jnxFruNotifAdminStatus.setStatus('current')
jnxFruNotifOperStatus = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 23, 3)).setObjects(("JUNIPER-FRU-MIB", "jnxFruCfgContentsIndex"), ("JUNIPER-FRU-MIB", "jnxFruCfgL1Index"), ("JUNIPER-FRU-MIB", "jnxFruCfgL2Index"), ("JUNIPER-FRU-MIB", "jnxFruCfgL3Index"), ("JUNIPER-FRU-MIB", "jnxFruCfgOperState"))
if mibBuilder.loadTexts: jnxFruNotifOperStatus.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-FRU-MIB", jnxFruNotifAdminStatus=jnxFruNotifAdminStatus, jnxFruCfg=jnxFruCfg, jnxFruCfgType=jnxFruCfgType, jnxFruMib=jnxFruMib, jnxFruCfgL3Index=jnxFruCfgL3Index, jnxFruNotifOperStatus=jnxFruNotifOperStatus, jnxFruCfgAdminState=jnxFruCfgAdminState, PYSNMP_MODULE_ID=jnxFruMib, jnxFruCfgL2Index=jnxFruCfgL2Index, jnxFruCfgL1Index=jnxFruCfgL1Index, JnxFruAdminStates=JnxFruAdminStates, jnxFruCfgOperState=jnxFruCfgOperState, jnxFruCfgTable=jnxFruCfgTable, jnxFruCfgContentsIndex=jnxFruCfgContentsIndex, jnxFruCfgEntry=jnxFruCfgEntry, JnxFruOperStates=JnxFruOperStates, jnxFruNotifMismatch=jnxFruNotifMismatch)
