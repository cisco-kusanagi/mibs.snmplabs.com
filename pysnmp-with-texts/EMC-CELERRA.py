#
# PySNMP MIB module EMC-CELERRA (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EMC-CELERRA
# Produced by pysmi-0.3.4 at Wed May  1 13:02:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, Counter64, NotificationType, enterprises, Opaque, iso, ModuleIdentity, Integer32, Unsigned32, IpAddress, Gauge32, MibIdentifier, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "Counter64", "NotificationType", "enterprises", "Opaque", "iso", "ModuleIdentity", "Integer32", "Unsigned32", "IpAddress", "Gauge32", "MibIdentifier", "Counter32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
emc = MibIdentifier((1, 3, 6, 1, 4, 1, 1139))
emcCelerra = MibIdentifier((1, 3, 6, 1, 4, 1, 1139, 2))
celEventTable = MibTable((1, 3, 6, 1, 4, 1, 1139, 2, 1), )
if mibBuilder.loadTexts: celEventTable.setStatus('mandatory')
if mibBuilder.loadTexts: celEventTable.setDescription('A table containing information about an particular event.')
celEvent = MibTableRow((1, 3, 6, 1, 4, 1, 1139, 2, 1, 1), ).setIndexNames((0, "EMC-CELERRA", "celEventFacility"), (0, "EMC-CELERRA", "celEventID"))
if mibBuilder.loadTexts: celEvent.setStatus('mandatory')
if mibBuilder.loadTexts: celEvent.setDescription('Information about an particular event.')
celEventFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 1139, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: celEventFacility.setStatus('mandatory')
if mibBuilder.loadTexts: celEventFacility.setDescription('The number representing the facility which generates the event. For now, the value could be: first 128 - default Dart facility 129 - master control 130 - event log 131 - box monitor 132 - video service 133 - callhome application 134 - AAF backup control station.')
celEventID = MibTableColumn((1, 3, 6, 1, 4, 1, 1139, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: celEventID.setStatus('mandatory')
if mibBuilder.loadTexts: celEventID.setDescription('The event id which identifies the particular event within a facility.')
celEventSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 1139, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: celEventSeverity.setStatus('mandatory')
if mibBuilder.loadTexts: celEventSeverity.setDescription('Severity of the event.')
celEventDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 1139, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: celEventDescr.setStatus('mandatory')
if mibBuilder.loadTexts: celEventDescr.setDescription('text description of the event.')
celReboot = NotificationType((1, 3, 6, 1, 4, 1, 1139, 2) + (0,1)).setObjects(("EMC-CELERRA", "celEvent"))
if mibBuilder.loadTexts: celReboot.setDescription('Trap message will be sent in the event of a Data Mover Reboots. The trap message includes the facility, event id, serverity and a text description of the event.')
celMasterCtlFault = NotificationType((1, 3, 6, 1, 4, 1, 1139, 2) + (0,2)).setObjects(("EMC-CELERRA", "celEvent"))
if mibBuilder.loadTexts: celMasterCtlFault.setDescription('Trap message will be sent in the event of Master Control serious fault. unexpected daemon exit or control station heartbeat missing.')
celHWFailure = NotificationType((1, 3, 6, 1, 4, 1, 1139, 2) + (0,3)).setObjects(("EMC-CELERRA", "celEvent"))
if mibBuilder.loadTexts: celHWFailure.setDescription('Trap message will be sent in the event of celerra hardware failure.')
celSlotStale = NotificationType((1, 3, 6, 1, 4, 1, 1139, 2) + (0,4)).setObjects(("EMC-CELERRA", "celEvent"))
if mibBuilder.loadTexts: celSlotStale.setDescription('Trap message will be sent in the event of celerra stale reason code.')
celSlotPanicked = NotificationType((1, 3, 6, 1, 4, 1, 1139, 2) + (0,5)).setObjects(("EMC-CELERRA", "celEvent"))
if mibBuilder.loadTexts: celSlotPanicked.setDescription('Trap message will be sent in the event of panicked slot.')
celIntfFailure = NotificationType((1, 3, 6, 1, 4, 1, 1139, 2) + (0,6)).setObjects(("EMC-CELERRA", "celEvent"))
if mibBuilder.loadTexts: celIntfFailure.setDescription('Trap message will be sent in the event of both interfaces failure.')
celAAF = NotificationType((1, 3, 6, 1, 4, 1, 1139, 2) + (0,7)).setObjects(("EMC-CELERRA", "celEvent"))
if mibBuilder.loadTexts: celAAF.setDescription('Trap message will be sent in the event of AAF.')
mibBuilder.exportSymbols("EMC-CELERRA", celHWFailure=celHWFailure, celReboot=celReboot, celEventDescr=celEventDescr, emcCelerra=emcCelerra, celAAF=celAAF, celEventFacility=celEventFacility, celEvent=celEvent, celMasterCtlFault=celMasterCtlFault, celIntfFailure=celIntfFailure, celSlotPanicked=celSlotPanicked, celEventID=celEventID, emc=emc, celSlotStale=celSlotStale, celEventSeverity=celEventSeverity, celEventTable=celEventTable)
