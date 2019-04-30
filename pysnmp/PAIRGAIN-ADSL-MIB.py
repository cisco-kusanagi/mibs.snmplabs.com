#
# PySNMP MIB module PAIRGAIN-ADSL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PAIRGAIN-ADSL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:27:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pgainDSLAM, = mibBuilder.importSymbols("PAIRGAIN-COMMON-HD-MIB", "pgainDSLAM")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, Counter32, Bits, Unsigned32, ModuleIdentity, IpAddress, NotificationType, MibIdentifier, ObjectIdentity, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "Counter32", "Bits", "Unsigned32", "ModuleIdentity", "IpAddress", "NotificationType", "MibIdentifier", "ObjectIdentity", "Gauge32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pgAdslMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 927, 1, 9, 15))
if mibBuilder.loadTexts: pgAdslMIB.setLastUpdated('')
if mibBuilder.loadTexts: pgAdslMIB.setOrganization('Pairgain Technology')
pgAdslMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 9, 15, 1))
pgAdslClearStatTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 9, 15, 1, 1), )
if mibBuilder.loadTexts: pgAdslClearStatTable.setStatus('current')
pgAdslClearStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 9, 15, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pgAdslClearStatEntry.setStatus('current')
pgAdslAtucClearStat = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 15, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgAdslAtucClearStat.setStatus('current')
pgAdslAturClearStat = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 15, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgAdslAturClearStat.setStatus('current')
mibBuilder.exportSymbols("PAIRGAIN-ADSL-MIB", PYSNMP_MODULE_ID=pgAdslMIB, pgAdslAtucClearStat=pgAdslAtucClearStat, pgAdslMIB=pgAdslMIB, pgAdslAturClearStat=pgAdslAturClearStat, pgAdslMIBObjects=pgAdslMIBObjects, pgAdslClearStatEntry=pgAdslClearStatEntry, pgAdslClearStatTable=pgAdslClearStatTable)
