#
# PySNMP MIB module SW3x12SRPRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW3x12SRPRIMGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:31:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
dlink_mgmt, dlink_products = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-mgmt", "dlink-products")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, IpAddress, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, Bits, Gauge32, MibIdentifier, ModuleIdentity, iso, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "Bits", "Gauge32", "MibIdentifier", "ModuleIdentity", "iso", "ObjectIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlink_Dgs3x12SRSeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 55)).setLabel("dlink-Dgs3x12SRSeriesProd")
dlink_Dgs3212SR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 55, 1)).setLabel("dlink-Dgs3212SR")
dlink_Dgs3312SR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 55, 2)).setLabel("dlink-Dgs3312SR")
dgs3x12SRSeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 55))
dgs3212SR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 55, 1))
dgs3312SR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 55, 2))
mibBuilder.exportSymbols("SW3x12SRPRIMGMT-MIB", dgs3312SR=dgs3312SR, dlink_Dgs3212SR=dlink_Dgs3212SR, dlink_Dgs3312SR=dlink_Dgs3312SR, dgs3x12SRSeriesProd=dgs3x12SRSeriesProd, dlink_Dgs3x12SRSeriesProd=dlink_Dgs3x12SRSeriesProd, dgs3212SR=dgs3212SR)
