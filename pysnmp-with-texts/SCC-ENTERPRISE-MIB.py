#
# PySNMP MIB module SCC-ENTERPRISE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SCC-ENTERPRISE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:01:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, enterprises, ModuleIdentity, ObjectIdentity, TimeTicks, IpAddress, Gauge32, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, Unsigned32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "enterprises", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "IpAddress", "Gauge32", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "Unsigned32", "Integer32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
scc = MibIdentifier((1, 3, 6, 1, 4, 1, 1386))
sccProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 1386, 1))
sccRaid7 = MibIdentifier((1, 3, 6, 1, 4, 1, 1386, 1, 1))
sccMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 1386, 2))
raid7mib = MibIdentifier((1, 3, 6, 1, 4, 1, 1386, 2, 1))
raid7proxy = MibIdentifier((1, 3, 6, 1, 4, 1, 1386, 2, 2))
mibBuilder.exportSymbols("SCC-ENTERPRISE-MIB", raid7proxy=raid7proxy, raid7mib=raid7mib, sccProducts=sccProducts, scc=scc, sccMibs=sccMibs, sccRaid7=sccRaid7)
