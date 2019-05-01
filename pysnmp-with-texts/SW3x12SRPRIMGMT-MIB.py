#
# PySNMP MIB module SW3x12SRPRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW3x12SRPRIMGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:46:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
dlink_products, dlink_mgmt = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products", "dlink-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, iso, Gauge32, ObjectIdentity, Unsigned32, NotificationType, Bits, Integer32, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "Gauge32", "ObjectIdentity", "Unsigned32", "NotificationType", "Bits", "Integer32", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlink_Dgs3x12SRSeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 55)).setLabel("dlink-Dgs3x12SRSeriesProd")
dlink_Dgs3212SR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 55, 1)).setLabel("dlink-Dgs3212SR")
dlink_Dgs3312SR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 55, 2)).setLabel("dlink-Dgs3312SR")
dgs3x12SRSeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 55))
dgs3212SR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 55, 1))
dgs3312SR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 55, 2))
mibBuilder.exportSymbols("SW3x12SRPRIMGMT-MIB", dlink_Dgs3x12SRSeriesProd=dlink_Dgs3x12SRSeriesProd, dgs3312SR=dgs3312SR, dlink_Dgs3312SR=dlink_Dgs3312SR, dgs3x12SRSeriesProd=dgs3x12SRSeriesProd, dgs3212SR=dgs3212SR, dlink_Dgs3212SR=dlink_Dgs3212SR)
