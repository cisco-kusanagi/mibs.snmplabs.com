#
# PySNMP MIB module DLINK-ID-REC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-ID-REC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:54:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, Integer32, ObjectIdentity, iso, Unsigned32, TimeTicks, MibIdentifier, enterprises, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "Integer32", "ObjectIdentity", "iso", "Unsigned32", "TimeTicks", "MibIdentifier", "enterprises", "Counter32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class AgentNotifyLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("critical", 0), ("warning", 1), ("information", 2), ("emergency", 3), ("alert", 4), ("error", 5), ("notice", 6), ("debug", 7))

dlink = MibIdentifier((1, 3, 6, 1, 4, 1, 171))
dlink_products = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10)).setLabel("dlink-products")
dlink_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11)).setLabel("dlink-mgmt")
dlink_common_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12)).setLabel("dlink-common-mgmt")
dlink_broadband_products = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 30)).setLabel("dlink-broadband-products")
dlink_broadband_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 31)).setLabel("dlink-broadband-mgmt")
mibBuilder.exportSymbols("DLINK-ID-REC-MIB", AgentNotifyLevel=AgentNotifyLevel, dlink_common_mgmt=dlink_common_mgmt, dlink_mgmt=dlink_mgmt, dlink=dlink, dlink_broadband_mgmt=dlink_broadband_mgmt, dlink_products=dlink_products, dlink_broadband_products=dlink_broadband_products)
