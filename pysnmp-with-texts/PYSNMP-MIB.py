#
# PySNMP MIB module PYSNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PYSNMP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:43:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, NotificationType, enterprises, IpAddress, Counter64, MibIdentifier, ObjectIdentity, ModuleIdentity, Counter32, iso, TimeTicks, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "NotificationType", "enterprises", "IpAddress", "Counter64", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Counter32", "iso", "TimeTicks", "Unsigned32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pysnmp = ModuleIdentity((1, 3, 6, 1, 4, 1, 20408))
pysnmp.setRevisions(('2017-04-14 00:00', '2005-05-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pysnmp.setRevisionsDescriptions(('Updated addresses', 'Initial revision',))
if mibBuilder.loadTexts: pysnmp.setLastUpdated('201704140000Z')
if mibBuilder.loadTexts: pysnmp.setOrganization('The PySNMP Project')
if mibBuilder.loadTexts: pysnmp.setContactInfo('E-mail: Ilya Etingof <etingof@gmail.com> GitHub: https://github.com/etingof/pysnmp')
if mibBuilder.loadTexts: pysnmp.setDescription('PySNMP top-level MIB tree infrastructure')
pysnmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 1))
pysnmpExamples = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 2))
pysnmpEnumerations = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 3))
pysnmpModuleIDs = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 3, 1))
pysnmpAgentOIDs = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 3, 2))
pysnmpDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 3, 3))
pysnmpExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 9999))
pysnmpNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 4))
pysnmpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 4, 0))
pysnmpNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 4, 1))
pysnmpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 5))
pysnmpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 5, 1))
pysnmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 5, 2))
mibBuilder.exportSymbols("PYSNMP-MIB", pysnmpNotifications=pysnmpNotifications, pysnmpObjects=pysnmpObjects, pysnmpGroups=pysnmpGroups, pysnmp=pysnmp, pysnmpNotificationObjects=pysnmpNotificationObjects, pysnmpExamples=pysnmpExamples, pysnmpCompliances=pysnmpCompliances, PYSNMP_MODULE_ID=pysnmp, pysnmpNotificationPrefix=pysnmpNotificationPrefix, pysnmpEnumerations=pysnmpEnumerations, pysnmpModuleIDs=pysnmpModuleIDs, pysnmpAgentOIDs=pysnmpAgentOIDs, pysnmpConformance=pysnmpConformance, pysnmpExperimental=pysnmpExperimental, pysnmpDomains=pysnmpDomains)
