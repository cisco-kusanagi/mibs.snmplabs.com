#
# PySNMP MIB module SW34XXPRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW34XXPRIMGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:31:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
dlink_products, dlink_mgmt = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products", "dlink-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibIdentifier, IpAddress, TimeTicks, Integer32, Counter32, iso, Gauge32, ObjectIdentity, Counter64, NotificationType, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "IpAddress", "TimeTicks", "Integer32", "Counter32", "iso", "Gauge32", "ObjectIdentity", "Counter64", "NotificationType", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlink_ProjectXStackIISeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70)).setLabel("dlink-ProjectXStackIISeriesProd")
dlink_Dgs3426 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 1)).setLabel("dlink-Dgs3426")
dlink_Dgs3427 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 2)).setLabel("dlink-Dgs3427")
dlink_Dgs3450 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 3)).setLabel("dlink-Dgs3450")
dlink_Dgs3426p = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 7)).setLabel("dlink-Dgs3426p")
dlink_Dgs3426g = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 11)).setLabel("dlink-Dgs3426g")
dgsProjectXStackIISeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70))
dgs3426 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 1))
dgs3427 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 2))
dgs3450 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 3))
dgs3426p = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 7))
dgs3426g = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 11))
mibBuilder.exportSymbols("SW34XXPRIMGMT-MIB", dgs3427=dgs3427, dlink_Dgs3427=dlink_Dgs3427, dlink_Dgs3426=dlink_Dgs3426, dgs3426=dgs3426, dlink_Dgs3426p=dlink_Dgs3426p, dlink_Dgs3426g=dlink_Dgs3426g, dgsProjectXStackIISeriesProd=dgsProjectXStackIISeriesProd, dgs3426g=dgs3426g, dgs3426p=dgs3426p, dgs3450=dgs3450, dlink_ProjectXStackIISeriesProd=dlink_ProjectXStackIISeriesProd, dlink_Dgs3450=dlink_Dgs3450)
