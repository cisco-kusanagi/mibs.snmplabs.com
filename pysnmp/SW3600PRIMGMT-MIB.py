#
# PySNMP MIB module SW3600PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW3600PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:05:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
dlink_products, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Bits, Counter64, IpAddress, iso, ModuleIdentity, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Bits", "Counter64", "IpAddress", "iso", "ModuleIdentity", "Counter32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dXS_3600Series = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 127)).setLabel("dXS-3600Series")
dXS_3600_32S = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 127, 1)).setLabel("dXS-3600-32S")
dXS_3600_16S = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 127, 2)).setLabel("dXS-3600-16S")
mibBuilder.exportSymbols("SW3600PRIMGMT-MIB", dXS_3600_32S=dXS_3600_32S, dXS_3600Series=dXS_3600Series, dXS_3600_16S=dXS_3600_16S)
