#
# PySNMP MIB module DGS-6600-ID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DGS-6600-ID-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:45:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
dlink_products, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, Bits, iso, Counter32, NotificationType, IpAddress, ModuleIdentity, ObjectIdentity, MibIdentifier, Gauge32, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "Bits", "iso", "Counter32", "NotificationType", "IpAddress", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "Gauge32", "Unsigned32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dgs6600Series = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120))
dgs6604 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 1))
dgs6608 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 2))
dgs6600Private = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100))
dgs6600_system = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1)).setLabel("dgs6600-system")
dgs6600_l2 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 2)).setLabel("dgs6600-l2")
dgs6600_l3 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 3)).setLabel("dgs6600-l3")
dgs6600_mpls = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4)).setLabel("dgs6600-mpls")
dgs6600_qosacl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 5)).setLabel("dgs6600-qosacl")
dgs6600_security = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 6)).setLabel("dgs6600-security")
dgs6600_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 7)).setLabel("dgs6600-mgmt")
dgs6600_others = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 8)).setLabel("dgs6600-others")
mibBuilder.exportSymbols("DGS-6600-ID-MIB", dgs6600_l3=dgs6600_l3, dgs6600_others=dgs6600_others, dgs6608=dgs6608, dgs6604=dgs6604, dgs6600Private=dgs6600Private, dgs6600_mpls=dgs6600_mpls, dgs6600_qosacl=dgs6600_qosacl, dgs6600_l2=dgs6600_l2, dgs6600_mgmt=dgs6600_mgmt, dgs6600_security=dgs6600_security, dgs6600_system=dgs6600_system, dgs6600Series=dgs6600Series)
