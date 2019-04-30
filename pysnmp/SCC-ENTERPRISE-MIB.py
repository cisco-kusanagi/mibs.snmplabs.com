#
# PySNMP MIB module SCC-ENTERPRISE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SCC-ENTERPRISE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:53:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, IpAddress, enterprises, Counter32, MibIdentifier, Gauge32, Bits, iso, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "IpAddress", "enterprises", "Counter32", "MibIdentifier", "Gauge32", "Bits", "iso", "Integer32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
scc = MibIdentifier((1, 3, 6, 1, 4, 1, 1386))
sccProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 1386, 1))
sccRaid7 = MibIdentifier((1, 3, 6, 1, 4, 1, 1386, 1, 1))
sccMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 1386, 2))
raid7mib = MibIdentifier((1, 3, 6, 1, 4, 1, 1386, 2, 1))
raid7proxy = MibIdentifier((1, 3, 6, 1, 4, 1, 1386, 2, 2))
mibBuilder.exportSymbols("SCC-ENTERPRISE-MIB", raid7proxy=raid7proxy, sccProducts=sccProducts, raid7mib=raid7mib, scc=scc, sccRaid7=sccRaid7, sccMibs=sccMibs)
