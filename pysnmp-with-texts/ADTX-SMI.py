#
# PySNMP MIB module ADTX-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADTX-SMI
# Produced by pysmi-0.3.4 at Wed May  1 11:15:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, MibIdentifier, enterprises, Counter64, Integer32, NotificationType, IpAddress, ObjectIdentity, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "MibIdentifier", "enterprises", "Counter64", "Integer32", "NotificationType", "IpAddress", "ObjectIdentity", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adtx = MibIdentifier((1, 3, 6, 1, 4, 1, 2653))
adtxReg = MibIdentifier((1, 3, 6, 1, 4, 1, 2653, 1))
adtxGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 2653, 2))
adtxProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 2653, 3))
adtxExpr = MibIdentifier((1, 3, 6, 1, 4, 1, 2653, 4))
mibBuilder.exportSymbols("ADTX-SMI", adtx=adtx, adtxReg=adtxReg, adtxGeneric=adtxGeneric, adtxExpr=adtxExpr, adtxProducts=adtxProducts)
