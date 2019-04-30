#
# PySNMP MIB module MICROSENS-G6-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MICROSENS-G6-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:04:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Bits, Counter32, NotificationType, Counter64, ObjectIdentity, TimeTicks, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, MibIdentifier, enterprises, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Counter32", "NotificationType", "Counter64", "ObjectIdentity", "TimeTicks", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "MibIdentifier", "enterprises", "ModuleIdentity")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
microsens = ModuleIdentity((1, 3, 6, 1, 4, 1, 3181))
microsens.setRevisions(('2015-05-22 10:58',))
if mibBuilder.loadTexts: microsens.setLastUpdated('201505221058Z')
if mibBuilder.loadTexts: microsens.setOrganization('MICROSENS GmbH & Co. KG')
managedSwitches = MibIdentifier((1, 3, 6, 1, 4, 1, 3181, 10))
g6 = MibIdentifier((1, 3, 6, 1, 4, 1, 3181, 10, 6))
mibBuilder.exportSymbols("MICROSENS-G6-MIB", PYSNMP_MODULE_ID=microsens, managedSwitches=managedSwitches, g6=g6, microsens=microsens)
