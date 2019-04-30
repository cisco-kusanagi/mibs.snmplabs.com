#
# PySNMP MIB module SCC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SCC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:53:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, enterprises, iso, Counter32, NotificationType, ModuleIdentity, Unsigned32, MibIdentifier, ObjectIdentity, Integer32, Bits, Gauge32, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "enterprises", "iso", "Counter32", "NotificationType", "ModuleIdentity", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Integer32", "Bits", "Gauge32", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
scc = MibIdentifier((1, 3, 6, 1, 4, 1, 1573))
sccExperiment = MibIdentifier((1, 3, 6, 1, 4, 1, 1573, 1))
sccProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 1573, 2))
sccMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 1573, 3))
sccSidewinder = MibIdentifier((1, 3, 6, 1, 4, 1, 1573, 2, 1))
sccSns = MibIdentifier((1, 3, 6, 1, 4, 1, 1573, 2, 2))
sccBfs = MibIdentifier((1, 3, 6, 1, 4, 1, 1573, 2, 3))
sccSecureZone = MibIdentifier((1, 3, 6, 1, 4, 1, 1573, 2, 4))
sccMibSw = MibIdentifier((1, 3, 6, 1, 4, 1, 1573, 3, 1))
sccMibSecureZone = MibIdentifier((1, 3, 6, 1, 4, 1, 1573, 3, 4))
mibBuilder.exportSymbols("SCC-MIB", sccMibs=sccMibs, scc=scc, sccSecureZone=sccSecureZone, sccSns=sccSns, sccMibSw=sccMibSw, sccMibSecureZone=sccMibSecureZone, sccExperiment=sccExperiment, sccProducts=sccProducts, sccSidewinder=sccSidewinder, sccBfs=sccBfs)
