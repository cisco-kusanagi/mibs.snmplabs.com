#
# PySNMP MIB module ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:03:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
dot1dBasePortEntry, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePortEntry")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, Gauge32, Unsigned32, iso, Counter32, ModuleIdentity, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, IpAddress, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "Unsigned32", "iso", "Counter32", "ModuleIdentity", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "IpAddress", "Counter64", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
etsysIetfpBridgeMibExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33))
etsysIetfpBridgeMibExtMIB.setRevisions(('2002-12-20 22:16',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: etsysIetfpBridgeMibExtMIB.setRevisionsDescriptions(('The initial version of this MIB module',))
if mibBuilder.loadTexts: etsysIetfpBridgeMibExtMIB.setLastUpdated('200212202216Z')
if mibBuilder.loadTexts: etsysIetfpBridgeMibExtMIB.setOrganization('Enterasys Networks, Inc')
if mibBuilder.loadTexts: etsysIetfpBridgeMibExtMIB.setContactInfo('Postal: Enterasys Networks 35 Industrial Way, P.O. Box 5005 Rochester, NH 03867-0505 Phone: +1 603 332 9400 E-mail: support@enterasys.com WWW: http://www.enterasys.com')
if mibBuilder.loadTexts: etsysIetfpBridgeMibExtMIB.setDescription("This MIB module defines a portion of the SNMP MIB under Enterasys Networks' enterprise OID pertaining to proprietary extensions to the IETF P-BRIDGE-MIB as specified in RFC2674.")
etsysIetfpBridgeMibExt = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 1))
etsysDot1dPriority = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 1, 1))
etsysDot1dPortPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 1, 1, 1), )
if mibBuilder.loadTexts: etsysDot1dPortPriorityTable.setStatus('current')
if mibBuilder.loadTexts: etsysDot1dPortPriorityTable.setDescription('Extensions to the table that contains information about every port that is associated with this transparent bridge.')
etsysDot1dPortPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 1, 1, 1, 1), )
dot1dBasePortEntry.registerAugmentions(("ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB", "etsysDot1dPortPriorityEntry"))
etsysDot1dPortPriorityEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
if mibBuilder.loadTexts: etsysDot1dPortPriorityEntry.setStatus('current')
if mibBuilder.loadTexts: etsysDot1dPortPriorityEntry.setDescription('A list of extensions that support the management of proprietary features for each port of a transparent bridge. This is indexed by dot1dBasePort.')
etsysDot1dPortPriorityRewrite = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 1, 1, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot1dPortPriorityRewrite.setStatus('current')
if mibBuilder.loadTexts: etsysDot1dPortPriorityRewrite.setDescription('The enabled/disabled status of the rewriting of the 802.1P priority in tagged frames on the port.')
etsysIetfpBridgeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 2))
etsysIetfpBridgeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 2, 1))
etsysIetfpBridgeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 2, 2))
etsysDot1dPriorityRewriteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 2, 1, 1)).setObjects(("ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB", "etsysDot1dPortPriorityRewrite"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDot1dPriorityRewriteGroup = etsysDot1dPriorityRewriteGroup.setStatus('current')
if mibBuilder.loadTexts: etsysDot1dPriorityRewriteGroup.setDescription('A collection of objects relating to the User Priority applicable to each port.')
etsysIetfpBridgeCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 2, 2, 1)).setObjects(("ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB", "etsysDot1dPriorityRewriteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIetfpBridgeCompliance = etsysIetfpBridgeCompliance.setStatus('current')
if mibBuilder.loadTexts: etsysIetfpBridgeCompliance.setDescription('The compliance statement for devices that support the IETF P-BRIDGE-MIB Extension MIB.')
mibBuilder.exportSymbols("ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB", etsysDot1dPortPriorityEntry=etsysDot1dPortPriorityEntry, etsysIetfpBridgeConformance=etsysIetfpBridgeConformance, etsysIetfpBridgeGroups=etsysIetfpBridgeGroups, etsysIetfpBridgeCompliances=etsysIetfpBridgeCompliances, etsysDot1dPriority=etsysDot1dPriority, etsysIetfpBridgeMibExt=etsysIetfpBridgeMibExt, etsysDot1dPortPriorityTable=etsysDot1dPortPriorityTable, PYSNMP_MODULE_ID=etsysIetfpBridgeMibExtMIB, etsysIetfpBridgeMibExtMIB=etsysIetfpBridgeMibExtMIB, etsysIetfpBridgeCompliance=etsysIetfpBridgeCompliance, etsysDot1dPortPriorityRewrite=etsysDot1dPortPriorityRewrite, etsysDot1dPriorityRewriteGroup=etsysDot1dPriorityRewriteGroup)
