#
# PySNMP MIB module CALIX-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CALIX-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 17:29:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, TimeTicks, ObjectIdentity, Gauge32, Counter64, ModuleIdentity, Integer32, Unsigned32, enterprises, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Gauge32", "Counter64", "ModuleIdentity", "Integer32", "Unsigned32", "enterprises", "Counter32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
calixNetworks = ModuleIdentity((1, 3, 6, 1, 4, 1, 6321))
calixNetworks.setRevisions(('2000-08-31 00:26',))
if mibBuilder.loadTexts: calixNetworks.setLastUpdated('200008310026Z')
if mibBuilder.loadTexts: calixNetworks.setOrganization('Calix Networks, Inc.')
calixRegistrations = ObjectIdentity((1, 3, 6, 1, 4, 1, 6321, 1))
if mibBuilder.loadTexts: calixRegistrations.setStatus('current')
calixModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 6321, 1, 1))
if mibBuilder.loadTexts: calixModules.setStatus('current')
calixProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 6321, 1, 2))
if mibBuilder.loadTexts: calixProducts.setStatus('current')
calixManagement = ObjectIdentity((1, 3, 6, 1, 4, 1, 6321, 2))
if mibBuilder.loadTexts: calixManagement.setStatus('current')
mibBuilder.exportSymbols("CALIX-SMI", PYSNMP_MODULE_ID=calixNetworks, calixRegistrations=calixRegistrations, calixModules=calixModules, calixProducts=calixProducts, calixNetworks=calixNetworks, calixManagement=calixManagement)
