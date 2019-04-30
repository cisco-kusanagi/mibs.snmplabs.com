#
# PySNMP MIB module TIARA-NETWORKS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIARA-NETWORKS-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 18:59:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, iso, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, ModuleIdentity, NotificationType, Unsigned32, TimeTicks, Counter32, MibIdentifier, Integer32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "ModuleIdentity", "NotificationType", "Unsigned32", "TimeTicks", "Counter32", "MibIdentifier", "Integer32", "Bits", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tiaraNetworks = ModuleIdentity((1, 3, 6, 1, 4, 1, 3174))
tiaraNetworks.setRevisions(('1993-04-01 00:00',))
if mibBuilder.loadTexts: tiaraNetworks.setLastUpdated('9904230000Z')
if mibBuilder.loadTexts: tiaraNetworks.setOrganization('Tiara Networks, Inc.')
tiaraProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 3174, 1))
if mibBuilder.loadTexts: tiaraProducts.setStatus('current')
tiaraMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 3174, 2))
if mibBuilder.loadTexts: tiaraMgmt.setStatus('current')
tiaraModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 3174, 3))
if mibBuilder.loadTexts: tiaraModules.setStatus('current')
tiaraExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 3174, 4))
if mibBuilder.loadTexts: tiaraExperiment.setStatus('current')
tiaraInterfaces = ObjectIdentity((1, 3, 6, 1, 4, 1, 3174, 2, 7))
if mibBuilder.loadTexts: tiaraInterfaces.setStatus('current')
mibBuilder.exportSymbols("TIARA-NETWORKS-SMI", tiaraNetworks=tiaraNetworks, tiaraInterfaces=tiaraInterfaces, tiaraModules=tiaraModules, tiaraMgmt=tiaraMgmt, tiaraExperiment=tiaraExperiment, tiaraProducts=tiaraProducts, PYSNMP_MODULE_ID=tiaraNetworks)
