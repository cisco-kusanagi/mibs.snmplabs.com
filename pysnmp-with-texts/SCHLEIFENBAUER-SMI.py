#
# PySNMP MIB module SCHLEIFENBAUER-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SCHLEIFENBAUER-SMI
# Produced by pysmi-0.3.4 at Wed May  1 15:01:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, IpAddress, ObjectIdentity, Gauge32, Counter32, ModuleIdentity, MibIdentifier, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, Unsigned32, enterprises, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "Counter32", "ModuleIdentity", "MibIdentifier", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "Unsigned32", "enterprises", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
schleifenbauer = ModuleIdentity((1, 3, 6, 1, 4, 1, 31034))
schleifenbauer.setRevisions(('2015-10-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: schleifenbauer.setRevisionsDescriptions(('The initial revision of this MIB module',))
if mibBuilder.loadTexts: schleifenbauer.setLastUpdated('201510230000Z')
if mibBuilder.loadTexts: schleifenbauer.setOrganization('Schleifenbauer Engineering')
if mibBuilder.loadTexts: schleifenbauer.setContactInfo('Schleifenbauer Engineering Alain Schuermans Chief Technology Officer Turnhoutseweg 22 5541 NX Reusel The Netherlands t. +31 73 5230256 f. +31 73 5212383 alain@schleifenbauer.eu www.schleifenbauer.eu')
if mibBuilder.loadTexts: schleifenbauer.setDescription('The Structure of Management Information for the Schleifenbauer enterprise. Copyright (c) 2015 by Schleifenbauer Products BV')
schleifenbauerProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 31034, 11))
if mibBuilder.loadTexts: schleifenbauerProducts.setStatus('current')
if mibBuilder.loadTexts: schleifenbauerProducts.setDescription('schleifenbauerProducts is the root OBJECT IDENTIFIER from which sysObjectId values are assigned. Acutal values are defined in SCHLEIFENBAUER-PRODUCTS-MIB.')
schleifenbauerMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 31034, 12))
if mibBuilder.loadTexts: schleifenbauerMgmt.setStatus('current')
if mibBuilder.loadTexts: schleifenbauerMgmt.setDescription('schleifenbauerMgmt is the main subtree for new mib development.')
schleifenbauerModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 31034, 13))
if mibBuilder.loadTexts: schleifenbauerModules.setStatus('current')
if mibBuilder.loadTexts: schleifenbauerModules.setDescription('schleifenbauerModules provides a root object identifier from which MODULE-IDENTITY values may be assigned.')
mibBuilder.exportSymbols("SCHLEIFENBAUER-SMI", schleifenbauer=schleifenbauer, schleifenbauerProducts=schleifenbauerProducts, schleifenbauerModules=schleifenbauerModules, schleifenbauerMgmt=schleifenbauerMgmt, PYSNMP_MODULE_ID=schleifenbauer)
