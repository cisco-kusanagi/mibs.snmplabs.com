#
# PySNMP MIB module FORCE10-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FORCE10-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 18:26:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Counter32, ModuleIdentity, NotificationType, MibIdentifier, IpAddress, Gauge32, Unsigned32, enterprises, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Counter32", "ModuleIdentity", "NotificationType", "MibIdentifier", "IpAddress", "Gauge32", "Unsigned32", "enterprises", "TimeTicks", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
force10 = ModuleIdentity((1, 3, 6, 1, 4, 1, 6027))
force10.setRevisions(('2007-06-15 12:00', '1900-10-10 00:00',))
if mibBuilder.loadTexts: force10.setLastUpdated('200706151200Z')
if mibBuilder.loadTexts: force10.setOrganization('Force10 Networks, Inc.')
f10Products = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 1))
if mibBuilder.loadTexts: f10Products.setStatus('current')
f10Common = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 2))
if mibBuilder.loadTexts: f10Common.setStatus('current')
f10Mgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 3))
if mibBuilder.loadTexts: f10Mgmt.setStatus('current')
f10Modules = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 4))
if mibBuilder.loadTexts: f10Modules.setStatus('current')
f10Experiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 20))
if mibBuilder.loadTexts: f10Experiment.setStatus('current')
mibBuilder.exportSymbols("FORCE10-SMI", f10Modules=f10Modules, f10Experiment=f10Experiment, f10Mgmt=f10Mgmt, force10=force10, f10Common=f10Common, f10Products=f10Products, PYSNMP_MODULE_ID=force10)
