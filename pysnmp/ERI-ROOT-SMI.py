#
# PySNMP MIB module ERI-ROOT-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ERI-ROOT-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 18:51:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, IpAddress, Unsigned32, MibIdentifier, enterprises, ObjectIdentity, Counter64, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, Bits, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "Unsigned32", "MibIdentifier", "enterprises", "ObjectIdentity", "Counter64", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "Bits", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eriEnterpriseRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 644))
virProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 1))
eriProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2))
eriMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 3))
mibBuilder.exportSymbols("ERI-ROOT-SMI", eriEnterpriseRoot=eriEnterpriseRoot, eriProducts=eriProducts, eriMibs=eriMibs, virProducts=virProducts)
