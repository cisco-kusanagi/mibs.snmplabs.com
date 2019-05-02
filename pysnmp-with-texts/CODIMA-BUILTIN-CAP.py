#
# PySNMP MIB module CODIMA-BUILTIN-CAP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CODIMA-BUILTIN-CAP
# Produced by pysmi-0.3.4 at Wed May  1 12:25:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
codimaCaps, = mibBuilder.importSymbols("CODIMA-GLOBAL-REG", "codimaCaps")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, Unsigned32, Counter32, MibIdentifier, Gauge32, IpAddress, Bits, TimeTicks, ObjectIdentity, iso, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "Unsigned32", "Counter32", "MibIdentifier", "Gauge32", "IpAddress", "Bits", "TimeTicks", "ObjectIdentity", "iso", "NotificationType", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
expressCapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 226, 4, 1))
expressCapMIB.setRevisions(('2003-06-17 11:27',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: expressCapMIB.setRevisionsDescriptions(('The initial version',))
if mibBuilder.loadTexts: expressCapMIB.setLastUpdated('200306171127Z')
if mibBuilder.loadTexts: expressCapMIB.setOrganization('CODIMA Technologies Ltd')
if mibBuilder.loadTexts: expressCapMIB.setContactInfo('support@codimatech.com')
if mibBuilder.loadTexts: expressCapMIB.setDescription('MIB module for CODIMA Express agent built-in capabilities.')
expressBuiltInCaps = AgentCapabilities((1, 3, 6, 1, 4, 1, 226, 4, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    expressBuiltInCaps = expressBuiltInCaps.setProductRelease('CODIMA Express v2.5')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    expressBuiltInCaps = expressBuiltInCaps.setStatus('current')
if mibBuilder.loadTexts: expressBuiltInCaps.setDescription('CODIMA Express Agent built-in capabilities.')
mibBuilder.exportSymbols("CODIMA-BUILTIN-CAP", expressBuiltInCaps=expressBuiltInCaps, expressCapMIB=expressCapMIB, PYSNMP_MODULE_ID=expressCapMIB)
