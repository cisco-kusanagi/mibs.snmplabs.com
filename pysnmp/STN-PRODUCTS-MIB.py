#
# PySNMP MIB module STN-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/STN-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:03:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
IpAddress, Unsigned32, MibIdentifier, Gauge32, Bits, iso, ModuleIdentity, Counter32, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "MibIdentifier", "Gauge32", "Bits", "iso", "ModuleIdentity", "Counter32", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stnProducts, stnMibModules = mibBuilder.importSymbols("SPRING-TIDE-NETWORKS-SMI", "stnProducts", "stnMibModules")
stnProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3551, 5, 2))
stnProductsMIB.setRevisions(('1999-05-01 00:00',))
if mibBuilder.loadTexts: stnProductsMIB.setLastUpdated('0002160000Z')
if mibBuilder.loadTexts: stnProductsMIB.setOrganization('Spring Tide Networks, Inc.')
stn5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 1, 1))
mibBuilder.exportSymbols("STN-PRODUCTS-MIB", stn5000=stn5000, PYSNMP_MODULE_ID=stnProductsMIB, stnProductsMIB=stnProductsMIB)
