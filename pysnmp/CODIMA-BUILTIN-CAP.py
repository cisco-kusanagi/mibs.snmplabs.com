#
# PySNMP MIB module CODIMA-BUILTIN-CAP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CODIMA-BUILTIN-CAP
# Produced by pysmi-0.3.4 at Mon Apr 29 18:09:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
codimaCaps, = mibBuilder.importSymbols("CODIMA-GLOBAL-REG", "codimaCaps")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, iso, MibIdentifier, Unsigned32, Integer32, IpAddress, Counter32, Gauge32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "iso", "MibIdentifier", "Unsigned32", "Integer32", "IpAddress", "Counter32", "Gauge32", "TimeTicks", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
expressCapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 226, 4, 1))
expressCapMIB.setRevisions(('2003-06-17 11:27',))
if mibBuilder.loadTexts: expressCapMIB.setLastUpdated('200306171127Z')
if mibBuilder.loadTexts: expressCapMIB.setOrganization('CODIMA Technologies Ltd')
expressBuiltInCaps = AgentCapabilities((1, 3, 6, 1, 4, 1, 226, 4, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    expressBuiltInCaps = expressBuiltInCaps.setProductRelease('CODIMA Express v2.5')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    expressBuiltInCaps = expressBuiltInCaps.setStatus('current')
mibBuilder.exportSymbols("CODIMA-BUILTIN-CAP", expressCapMIB=expressCapMIB, expressBuiltInCaps=expressBuiltInCaps, PYSNMP_MODULE_ID=expressCapMIB)
