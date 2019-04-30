#
# PySNMP MIB module ADTX-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADTX-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 16:59:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, enterprises, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, TimeTicks, Unsigned32, ObjectIdentity, Gauge32, MibIdentifier, iso, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "enterprises", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "TimeTicks", "Unsigned32", "ObjectIdentity", "Gauge32", "MibIdentifier", "iso", "Bits", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adtx = MibIdentifier((1, 3, 6, 1, 4, 1, 2653))
adtxReg = MibIdentifier((1, 3, 6, 1, 4, 1, 2653, 1))
adtxGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 2653, 2))
adtxProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 2653, 3))
adtxExpr = MibIdentifier((1, 3, 6, 1, 4, 1, 2653, 4))
mibBuilder.exportSymbols("ADTX-SMI", adtxGeneric=adtxGeneric, adtx=adtx, adtxExpr=adtxExpr, adtxReg=adtxReg, adtxProducts=adtxProducts)
