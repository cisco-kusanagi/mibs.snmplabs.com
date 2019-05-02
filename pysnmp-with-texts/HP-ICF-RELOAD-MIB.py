#
# PySNMP MIB module HP-ICF-RELOAD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-RELOAD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:35:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
hpicfBasic, = mibBuilder.importSymbols("HP-ICF-BASIC", "hpicfBasic")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, Unsigned32, Bits, TimeTicks, Integer32, MibIdentifier, ModuleIdentity, Gauge32, iso, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "Unsigned32", "Bits", "TimeTicks", "Integer32", "MibIdentifier", "ModuleIdentity", "Gauge32", "iso", "IpAddress", "NotificationType")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
hpicfReloadMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20))
hpicfReloadMIB.setRevisions(('2009-12-03 00:00', '2009-10-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfReloadMIB.setRevisionsDescriptions(('Added object hpicfReloadTable ', 'Added objects hpicfReloadState, hpicfReloadAfter, hpicfReloadAt',))
if mibBuilder.loadTexts: hpicfReloadMIB.setLastUpdated('200912030000Z')
if mibBuilder.loadTexts: hpicfReloadMIB.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfReloadMIB.setContactInfo('Hewlett Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfReloadMIB.setDescription('This MIB module describes objects for basic management of reloading devices in the HP Integrated Communication Facility product line.')
hpicfReloadObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 1))
hpicfEntityReload = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 2))
hpicfReloadConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3))
class ReloadControl(TextualConvention, Integer32):
    description = 'An enumerated value which provides an indication of the reload control.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("reloadSlotNone", 1), ("fullPowerCycleReload", 2))

hpicfReloadState = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notScheduled", 1), ("reloadAfter", 2), ("reloadAt", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfReloadState.setStatus('current')
if mibBuilder.loadTexts: hpicfReloadState.setDescription("This object specifies the state of the device. If it is in: (1) 'no reload' was scheduled (2) 'reload after' was scheduled (3) 'reload at' was scheduled To cancel the scheduled reload, this object needs to be set with (1). NOTE: This object cannot be set with (2) or (3).When hpicfReloadAfter or hpicfReloadAt is scheduled the state of hpicfReloadState is automatically changed to (2) or (3) respectively.")
hpicfReloadAfter = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfReloadAfter.setStatus('current')
if mibBuilder.loadTexts: hpicfReloadAfter.setDescription('The object specifies the time in seconds after which reload will occur.If no reload is scheduled it returns -1. To schedule a reload/reboot, time in seconds is entered and 0 for immediate reload. When hpicfReloadAfter is scheduled the state of hpicfReloadState is changed to reloadAfter automatically. NOTE: If hpicfReloadAt or hpicfReloadAfter is already scheduled, it will automatically be cancelled and the new hpicfReloadAfter is scheduled.')
hpicfReloadAt = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 1, 3), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfReloadAt.setStatus('current')
if mibBuilder.loadTexts: hpicfReloadAt.setDescription('The object specifies the time and date at which reload will occur. To schedule a reload in the future, the time and date at which reload needs to occur should be given. When hpicfReloadAt is scheduled it will change the state of hpicfReloadState to reloadAt. NOTE: If hpicfReloadAt or hpicfReloadAfter is already scheduled, it will automatically be cancelled and the new hpicfReloadAt is scheduled.')
hpicfReloadTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 2, 2), )
if mibBuilder.loadTexts: hpicfReloadTable.setStatus('current')
if mibBuilder.loadTexts: hpicfReloadTable.setDescription('This table contains a row for different entities and shows the control operation and the latest reload time for that entity.')
hpicfReloadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 2, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hpicfReloadEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfReloadEntry.setDescription('Information about Reload table.')
hpicfReloadControl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 2, 2, 1, 1), ReloadControl()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfReloadControl.setStatus('current')
if mibBuilder.loadTexts: hpicfReloadControl.setDescription('This specifies the control action for this entity')
hpicfReloadDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 2, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfReloadDateTime.setStatus('current')
if mibBuilder.loadTexts: hpicfReloadDateTime.setDescription('The object specifies the time and date at which the last reload will occured')
hpicfReloadGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 1))
hpicfReloadCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 2))
hpicfReloadGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 1, 1)).setObjects(("HP-ICF-RELOAD-MIB", "hpicfReloadState"), ("HP-ICF-RELOAD-MIB", "hpicfReloadAfter"), ("HP-ICF-RELOAD-MIB", "hpicfReloadAt"), ("HP-ICF-RELOAD-MIB", "hpicfReloadControl"), ("HP-ICF-RELOAD-MIB", "hpicfReloadDateTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfReloadGroup = hpicfReloadGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfReloadGroup.setDescription('A collection of objects for reload command.')
hpicfReloadFullCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 2, 1)).setObjects(("HP-ICF-RELOAD-MIB", "hpicfReloadGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfReloadFullCompliance1 = hpicfReloadFullCompliance1.setStatus('current')
if mibBuilder.loadTexts: hpicfReloadFullCompliance1.setDescription('The compliance statement for SNMP entities which implement the RELOAD-MIB with support for writable objects and notifications. Such an implementation can be both monitored and configured via SNMP. It can also send notifications about change in the operational status of the Reload application. ')
hpicfReloadFullCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 2, 2)).setObjects(("HP-ICF-RELOAD-MIB", "hpicfReloadGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfReloadFullCompliance2 = hpicfReloadFullCompliance2.setStatus('current')
if mibBuilder.loadTexts: hpicfReloadFullCompliance2.setDescription('The compliance statement for SNMP entities which implement the RELOAD-MIB with support for writable objects. Such an implementation can be both monitored and configured via SNMP. ')
hpicfReloadReadOnlyCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 2, 3)).setObjects(("HP-ICF-RELOAD-MIB", "hpicfReloadGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfReloadReadOnlyCompliance1 = hpicfReloadReadOnlyCompliance1.setStatus('current')
if mibBuilder.loadTexts: hpicfReloadReadOnlyCompliance1.setDescription('The compliance statement for SNMP entities which implement the hpicfReload MIB without support for read-write (i.e. in read-only mode). It can also send notifications about change in the operational status of the syslog application. ')
mibBuilder.exportSymbols("HP-ICF-RELOAD-MIB", hpicfReloadEntry=hpicfReloadEntry, hpicfReloadDateTime=hpicfReloadDateTime, hpicfReloadMIB=hpicfReloadMIB, hpicfEntityReload=hpicfEntityReload, hpicfReloadState=hpicfReloadState, hpicfReloadConformance=hpicfReloadConformance, hpicfReloadAt=hpicfReloadAt, hpicfReloadAfter=hpicfReloadAfter, hpicfReloadTable=hpicfReloadTable, hpicfReloadReadOnlyCompliance1=hpicfReloadReadOnlyCompliance1, hpicfReloadObjects=hpicfReloadObjects, hpicfReloadGroup=hpicfReloadGroup, hpicfReloadFullCompliance1=hpicfReloadFullCompliance1, ReloadControl=ReloadControl, PYSNMP_MODULE_ID=hpicfReloadMIB, hpicfReloadGroups=hpicfReloadGroups, hpicfReloadFullCompliance2=hpicfReloadFullCompliance2, hpicfReloadControl=hpicfReloadControl, hpicfReloadCompliances=hpicfReloadCompliances)
