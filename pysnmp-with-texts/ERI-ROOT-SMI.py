#
# PySNMP MIB module ERI-ROOT-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ERI-ROOT-SMI
# Produced by pysmi-0.3.4 at Wed May  1 13:05:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, iso, MibIdentifier, TimeTicks, Gauge32, ObjectIdentity, Integer32, IpAddress, NotificationType, Unsigned32, Counter32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "MibIdentifier", "TimeTicks", "Gauge32", "ObjectIdentity", "Integer32", "IpAddress", "NotificationType", "Unsigned32", "Counter32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eriEnterpriseRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 644))
virProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 1))
eriProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2))
eriMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 3))
mibBuilder.exportSymbols("ERI-ROOT-SMI", eriEnterpriseRoot=eriEnterpriseRoot, eriProducts=eriProducts, eriMibs=eriMibs, virProducts=virProducts)
