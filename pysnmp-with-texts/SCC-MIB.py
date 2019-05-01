#
# PySNMP MIB module SCC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SCC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:01:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, Bits, Unsigned32, Integer32, Gauge32, Counter64, IpAddress, NotificationType, MibIdentifier, iso, ObjectIdentity, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Bits", "Unsigned32", "Integer32", "Gauge32", "Counter64", "IpAddress", "NotificationType", "MibIdentifier", "iso", "ObjectIdentity", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
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
mibBuilder.exportSymbols("SCC-MIB", sccBfs=sccBfs, sccMibSecureZone=sccMibSecureZone, sccSecureZone=sccSecureZone, sccSns=sccSns, sccMibs=sccMibs, sccMibSw=sccMibSw, sccExperiment=sccExperiment, sccSidewinder=sccSidewinder, scc=scc, sccProducts=sccProducts)
