#
# PySNMP MIB module CERENT-IF-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CERENT-IF-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:48:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
cerentRequirements, cerentModules, cerentGeneric = mibBuilder.importSymbols("CERENT-GLOBAL-REGISTRY", "cerentRequirements", "cerentModules", "cerentGeneric")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, Counter64, Gauge32, ObjectIdentity, MibIdentifier, TimeTicks, Counter32, Integer32, Bits, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "Counter64", "Gauge32", "ObjectIdentity", "MibIdentifier", "TimeTicks", "Counter32", "Integer32", "Bits", "NotificationType", "Unsigned32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
cerentIfExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3607, 1, 10, 140))
cerentIfExtMIB.setRevisions(('2005-11-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cerentIfExtMIB.setRevisionsDescriptions(('Inital version of the module',))
if mibBuilder.loadTexts: cerentIfExtMIB.setLastUpdated('200511140000Z')
if mibBuilder.loadTexts: cerentIfExtMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cerentIfExtMIB.setContactInfo(' support@Cisco.com Postal: Cisco Systems 1450 N. McDowell Blvd. Petaluma, CA 94954 USA Tel: +1-877-323-7368')
if mibBuilder.loadTexts: cerentIfExtMIB.setDescription('This module defines objects for managing interfaces.')
cerentIfExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3607, 2, 100))
cerentIfExtTable = MibTable((1, 3, 6, 1, 4, 1, 3607, 2, 100, 10), )
if mibBuilder.loadTexts: cerentIfExtTable.setStatus('current')
if mibBuilder.loadTexts: cerentIfExtTable.setDescription('This table contains one row per interface.')
cerentIfExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cerentIfExtEntry.setStatus('current')
if mibBuilder.loadTexts: cerentIfExtEntry.setDescription('Row definition for cerentIfExtTable')
cerentIfExtPreServiceAlarmSuppression = MibTableColumn((1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1, 10), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cerentIfExtPreServiceAlarmSuppression.setStatus('current')
if mibBuilder.loadTexts: cerentIfExtPreServiceAlarmSuppression.setDescription("This object can be set through a management interface. When the administrative state of this interface is 'down', the value of this object does not have any impact. When the administrative state of this interface is 'up', if this object has a value of 'false', an alarm on this interface will be reported. If the value of this object is 'true' then all alarms on this interface will be suppressed. If the interface has a good signal, the soak timer will be started, if the port is faulted before the soak timer expires, the soak timer will be reset to the provisioned maximum value. If the soak timer expires then the value of this object is automatically set to 'false'.")
cerentIfExtConfiguredSoakTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1, 20), Integer32().clone(480)).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cerentIfExtConfiguredSoakTime.setStatus('current')
if mibBuilder.loadTexts: cerentIfExtConfiguredSoakTime.setDescription('This is the configured maximum value of the soak timer for this interface.')
cerentIfExtCurrentSoakTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1, 30), Integer32()).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cerentIfExtCurrentSoakTime.setStatus('current')
if mibBuilder.loadTexts: cerentIfExtCurrentSoakTime.setDescription('This is the current value of the soak timer for this interface. The difference between cerntIfExtConfiguredSoakTime and this object gives the time duration for which this interface has had a good signal.')
cerentIfExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3607, 5, 90))
cerentIfExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3607, 5, 90, 1))
cerentIfExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3607, 5, 90, 2))
cerentIfExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3607, 5, 90, 1, 1)).setObjects(("CERENT-IF-EXT-MIB", "cerentIfExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cerentIfExtMIBCompliance = cerentIfExtMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cerentIfExtMIBCompliance.setDescription('Describes the requirements for conformance to the High Capacity Media Independent Group.')
cerentIfExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3607, 5, 90, 2, 10)).setObjects(("CERENT-IF-EXT-MIB", "cerentIfExtPreServiceAlarmSuppression"), ("CERENT-IF-EXT-MIB", "cerentIfExtConfiguredSoakTime"), ("CERENT-IF-EXT-MIB", "cerentIfExtCurrentSoakTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cerentIfExtGroup = cerentIfExtGroup.setStatus('current')
if mibBuilder.loadTexts: cerentIfExtGroup.setDescription('The objects for storing all the current alarm thresholds ')
mibBuilder.exportSymbols("CERENT-IF-EXT-MIB", cerentIfExtConfiguredSoakTime=cerentIfExtConfiguredSoakTime, cerentIfExtMIBObjects=cerentIfExtMIBObjects, cerentIfExtMIBGroups=cerentIfExtMIBGroups, PYSNMP_MODULE_ID=cerentIfExtMIB, cerentIfExtMIBCompliances=cerentIfExtMIBCompliances, cerentIfExtMIB=cerentIfExtMIB, cerentIfExtPreServiceAlarmSuppression=cerentIfExtPreServiceAlarmSuppression, cerentIfExtMIBConformance=cerentIfExtMIBConformance, cerentIfExtGroup=cerentIfExtGroup, cerentIfExtEntry=cerentIfExtEntry, cerentIfExtTable=cerentIfExtTable, cerentIfExtMIBCompliance=cerentIfExtMIBCompliance, cerentIfExtCurrentSoakTime=cerentIfExtCurrentSoakTime)
