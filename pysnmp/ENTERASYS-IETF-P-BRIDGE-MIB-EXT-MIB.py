#
# PySNMP MIB module ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:49:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
dot1dBasePortEntry, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePortEntry")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, Counter64, Counter32, NotificationType, TimeTicks, IpAddress, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, ObjectIdentity, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Counter32", "NotificationType", "TimeTicks", "IpAddress", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "ObjectIdentity", "iso", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
etsysIetfpBridgeMibExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33))
etsysIetfpBridgeMibExtMIB.setRevisions(('2002-12-20 22:16',))
if mibBuilder.loadTexts: etsysIetfpBridgeMibExtMIB.setLastUpdated('200212202216Z')
if mibBuilder.loadTexts: etsysIetfpBridgeMibExtMIB.setOrganization('Enterasys Networks, Inc')
etsysIetfpBridgeMibExt = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 1))
etsysDot1dPriority = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 1, 1))
etsysDot1dPortPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 1, 1, 1), )
if mibBuilder.loadTexts: etsysDot1dPortPriorityTable.setStatus('current')
etsysDot1dPortPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 1, 1, 1, 1), )
dot1dBasePortEntry.registerAugmentions(("ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB", "etsysDot1dPortPriorityEntry"))
etsysDot1dPortPriorityEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
if mibBuilder.loadTexts: etsysDot1dPortPriorityEntry.setStatus('current')
etsysDot1dPortPriorityRewrite = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 1, 1, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot1dPortPriorityRewrite.setStatus('current')
etsysIetfpBridgeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 2))
etsysIetfpBridgeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 2, 1))
etsysIetfpBridgeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 2, 2))
etsysDot1dPriorityRewriteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 2, 1, 1)).setObjects(("ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB", "etsysDot1dPortPriorityRewrite"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDot1dPriorityRewriteGroup = etsysDot1dPriorityRewriteGroup.setStatus('current')
etsysIetfpBridgeCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 2, 2, 1)).setObjects(("ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB", "etsysDot1dPriorityRewriteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIetfpBridgeCompliance = etsysIetfpBridgeCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB", etsysDot1dPortPriorityTable=etsysDot1dPortPriorityTable, etsysIetfpBridgeConformance=etsysIetfpBridgeConformance, etsysIetfpBridgeCompliances=etsysIetfpBridgeCompliances, etsysDot1dPriority=etsysDot1dPriority, etsysIetfpBridgeGroups=etsysIetfpBridgeGroups, etsysIetfpBridgeCompliance=etsysIetfpBridgeCompliance, etsysIetfpBridgeMibExtMIB=etsysIetfpBridgeMibExtMIB, PYSNMP_MODULE_ID=etsysIetfpBridgeMibExtMIB, etsysDot1dPortPriorityEntry=etsysDot1dPortPriorityEntry, etsysIetfpBridgeMibExt=etsysIetfpBridgeMibExt, etsysDot1dPriorityRewriteGroup=etsysDot1dPriorityRewriteGroup, etsysDot1dPortPriorityRewrite=etsysDot1dPortPriorityRewrite)
