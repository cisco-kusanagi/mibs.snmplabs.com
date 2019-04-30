#
# PySNMP MIB module SW36XXPRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW36XXPRIMGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:31:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
dlink_products, dlink_mgmt = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products", "dlink-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Bits, MibIdentifier, TimeTicks, Counter64, NotificationType, ModuleIdentity, Counter32, iso, Integer32, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Bits", "MibIdentifier", "TimeTicks", "Counter64", "NotificationType", "ModuleIdentity", "Counter32", "iso", "Integer32", "Gauge32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlink_ProjectXStackIISeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70)).setLabel("dlink-ProjectXStackIISeriesProd")
dlink_Dgs3650 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 5)).setLabel("dlink-Dgs3650")
dlink_Dgs3627 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 6)).setLabel("dlink-Dgs3627")
dlink_Dgs3627g = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 8)).setLabel("dlink-Dgs3627g")
dlink_Dgs3612g = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 9)).setLabel("dlink-Dgs3612g")
dlink_Dgs3612 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 10)).setLabel("dlink-Dgs3612")
dgsProjectXStackIISeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70))
dgs3650 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 5))
dgs3627 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 6))
dgs3627g = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 8))
dgs3612g = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 9))
dgs3612 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 10))
mibBuilder.exportSymbols("SW36XXPRIMGMT-MIB", dlink_Dgs3627g=dlink_Dgs3627g, dlink_ProjectXStackIISeriesProd=dlink_ProjectXStackIISeriesProd, dgs3627=dgs3627, dgsProjectXStackIISeriesProd=dgsProjectXStackIISeriesProd, dlink_Dgs3627=dlink_Dgs3627, dgs3627g=dgs3627g, dlink_Dgs3612g=dlink_Dgs3612g, dgs3612=dgs3612, dgs3650=dgs3650, dlink_Dgs3612=dlink_Dgs3612, dlink_Dgs3650=dlink_Dgs3650, dgs3612g=dgs3612g)
