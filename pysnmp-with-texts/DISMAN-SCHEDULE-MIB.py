#
# PySNMP MIB module DISMAN-SCHEDULE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DISMAN-SCHEDULE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:13:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, iso, MibIdentifier, ModuleIdentity, Unsigned32, Integer32, Gauge32, IpAddress, NotificationType, zeroDotZero, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, mib_2, Counter32, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Integer32", "Gauge32", "IpAddress", "NotificationType", "zeroDotZero", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "mib-2", "Counter32", "Bits", "TimeTicks")
DisplayString, DateAndTime, RowStatus, StorageType, VariablePointer, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "RowStatus", "StorageType", "VariablePointer", "TextualConvention")
schedMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 63))
schedMIB.setRevisions(('2002-01-07 00:00', '1998-11-17 18:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: schedMIB.setRevisionsDescriptions(('Revised version, published as RFC 3231. This revision introduces a new object type called schedTriggers. Created new conformance and compliance statements that take care of the new schedTriggers object. Several clarifications have been added to remove ambiguities that were discovered and reported by implementors.', 'Initial version, published as RFC 2591.',))
if mibBuilder.loadTexts: schedMIB.setLastUpdated('200201070000Z')
if mibBuilder.loadTexts: schedMIB.setOrganization('IETF Distributed Management Working Group')
if mibBuilder.loadTexts: schedMIB.setContactInfo('WG EMail: disman@dorothy.bmc.com Subscribe: disman-request@dorothy.bmc.com Chair: Randy Presuhn BMC Software, Inc. Postal: Office 1-3141 2141 North First Street San Jose, California 95131 USA EMail: rpresuhn@bmc.com Phone: +1 408 546-1006 Editor: David B. Levi Nortel Networks Postal: 4401 Great America Parkway Santa Clara, CA 95052-8185 USA EMail: dlevi@nortelnetworks.com Phone: +1 865 686 0432 Editor: Juergen Schoenwaelder TU Braunschweig Postal: Bueltenweg 74/75 38106 Braunschweig Germany EMail: schoenw@ibr.cs.tu-bs.de Phone: +49 531 391-3283')
if mibBuilder.loadTexts: schedMIB.setDescription('This MIB module defines a MIB which provides mechanisms to schedule SNMP set operations periodically or at specific points in time.')
schedObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 1))
schedNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 2))
schedConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 3))
class SnmpPduErrorStatus(TextualConvention, Integer32):
    description = "This TC enumerates the SNMPv1 and SNMPv2 PDU error status codes as defined in RFC 1157 and RFC 1905. It also adds a pseudo error status code `noResponse' which indicates a timeout condition."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("noResponse", -1), ("noError", 0), ("tooBig", 1), ("noSuchName", 2), ("badValue", 3), ("readOnly", 4), ("genErr", 5), ("noAccess", 6), ("wrongType", 7), ("wrongLength", 8), ("wrongEncoding", 9), ("wrongValue", 10), ("noCreation", 11), ("inconsistentValue", 12), ("resourceUnavailable", 13), ("commitFailed", 14), ("undoFailed", 15), ("authorizationError", 16), ("notWritable", 17), ("inconsistentName", 18))

schedLocalTime = MibScalar((1, 3, 6, 1, 2, 1, 63, 1, 1), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(11, 11)).setFixedLength(11)).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedLocalTime.setStatus('current')
if mibBuilder.loadTexts: schedLocalTime.setDescription('The local time used by the scheduler. Schedules which refer to calendar time will use the local time indicated by this object. An implementation MUST return all 11 bytes of the DateAndTime textual-convention so that a manager may retrieve the offset from GMT time.')
schedTable = MibTable((1, 3, 6, 1, 2, 1, 63, 1, 2), )
if mibBuilder.loadTexts: schedTable.setStatus('current')
if mibBuilder.loadTexts: schedTable.setDescription('This table defines scheduled actions triggered by SNMP set operations.')
schedEntry = MibTableRow((1, 3, 6, 1, 2, 1, 63, 1, 2, 1), ).setIndexNames((0, "DISMAN-SCHEDULE-MIB", "schedOwner"), (0, "DISMAN-SCHEDULE-MIB", "schedName"))
if mibBuilder.loadTexts: schedEntry.setStatus('current')
if mibBuilder.loadTexts: schedEntry.setDescription('An entry describing a particular scheduled action. Unless noted otherwise, writable objects of this row can be modified independent of the current value of schedRowStatus, schedAdminStatus and schedOperStatus. In particular, it is legal to modify schedInterval and the objects in the schedCalendarGroup when schedRowStatus is active and schedAdminStatus and schedOperStatus are both enabled.')
schedOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: schedOwner.setStatus('current')
if mibBuilder.loadTexts: schedOwner.setDescription('The owner of this scheduling entry. The exact semantics of this string are subject to the security policy defined by the security administrator.')
schedName = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: schedName.setStatus('current')
if mibBuilder.loadTexts: schedName.setDescription('The locally-unique, administratively assigned name for this scheduling entry. This object allows a schedOwner to have multiple entries in the schedTable.')
schedDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedDescr.setStatus('current')
if mibBuilder.loadTexts: schedDescr.setDescription('The human readable description of the purpose of this scheduling entry.')
schedInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 4), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedInterval.setStatus('current')
if mibBuilder.loadTexts: schedInterval.setDescription('The number of seconds between two action invocations of a periodic scheduler. Implementations must guarantee that action invocations will not occur before at least schedInterval seconds have passed. The scheduler must ignore all periodic schedules that have a schedInterval value of 0. A periodic schedule with a scheduling interval of 0 seconds will therefore never invoke an action. Implementations may be forced to delay invocations in the face of local constraints. A scheduled management function should therefore not rely on the accuracy provided by the scheduler implementation. Note that implementations which maintain a list of pending activations must re-calculate them when this object is changed.')
schedWeekDay = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 5), Bits().clone(namedValues=NamedValues(("sunday", 0), ("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedWeekDay.setStatus('current')
if mibBuilder.loadTexts: schedWeekDay.setDescription('The set of weekdays on which the scheduled action should take place. Setting multiple bits will include several weekdays in the set of possible weekdays for this schedule. Setting all bits will cause the scheduler to ignore the weekday. Note that implementations which maintain a list of pending activations must re-calculate them when this object is changed.')
schedMonth = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 6), Bits().clone(namedValues=NamedValues(("january", 0), ("february", 1), ("march", 2), ("april", 3), ("may", 4), ("june", 5), ("july", 6), ("august", 7), ("september", 8), ("october", 9), ("november", 10), ("december", 11)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedMonth.setStatus('current')
if mibBuilder.loadTexts: schedMonth.setDescription('The set of months during which the scheduled action should take place. Setting multiple bits will include several months in the set of possible months for this schedule. Setting all bits will cause the scheduler to ignore the month. Note that implementations which maintain a list of pending activations must re-calculate them when this object is changed.')
schedDay = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 7), Bits().clone(namedValues=NamedValues(("d1", 0), ("d2", 1), ("d3", 2), ("d4", 3), ("d5", 4), ("d6", 5), ("d7", 6), ("d8", 7), ("d9", 8), ("d10", 9), ("d11", 10), ("d12", 11), ("d13", 12), ("d14", 13), ("d15", 14), ("d16", 15), ("d17", 16), ("d18", 17), ("d19", 18), ("d20", 19), ("d21", 20), ("d22", 21), ("d23", 22), ("d24", 23), ("d25", 24), ("d26", 25), ("d27", 26), ("d28", 27), ("d29", 28), ("d30", 29), ("d31", 30), ("r1", 31), ("r2", 32), ("r3", 33), ("r4", 34), ("r5", 35), ("r6", 36), ("r7", 37), ("r8", 38), ("r9", 39), ("r10", 40), ("r11", 41), ("r12", 42), ("r13", 43), ("r14", 44), ("r15", 45), ("r16", 46), ("r17", 47), ("r18", 48), ("r19", 49), ("r20", 50), ("r21", 51), ("r22", 52), ("r23", 53), ("r24", 54), ("r25", 55), ("r26", 56), ("r27", 57), ("r28", 58), ("r29", 59), ("r30", 60), ("r31", 61)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedDay.setStatus('current')
if mibBuilder.loadTexts: schedDay.setDescription("The set of days in a month on which a scheduled action should take place. There are two sets of bits one can use to define the day within a month: Enumerations starting with the letter 'd' indicate a day in a month relative to the first day of a month. The first day of the month can therefore be specified by setting the bit d1(0) and d31(30) means the last day of a month with 31 days. Enumerations starting with the letter 'r' indicate a day in a month in reverse order, relative to the last day of a month. The last day in the month can therefore be specified by setting the bit r1(31) and r31(61) means the first day of a month with 31 days. Setting multiple bits will include several days in the set of possible days for this schedule. Setting all bits will cause the scheduler to ignore the day within a month. Setting all bits starting with the letter 'd' or the letter 'r' will also cause the scheduler to ignore the day within a month. Note that implementations which maintain a list of pending activations must re-calculate them when this object is changed.")
schedHour = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 8), Bits().clone(namedValues=NamedValues(("h0", 0), ("h1", 1), ("h2", 2), ("h3", 3), ("h4", 4), ("h5", 5), ("h6", 6), ("h7", 7), ("h8", 8), ("h9", 9), ("h10", 10), ("h11", 11), ("h12", 12), ("h13", 13), ("h14", 14), ("h15", 15), ("h16", 16), ("h17", 17), ("h18", 18), ("h19", 19), ("h20", 20), ("h21", 21), ("h22", 22), ("h23", 23)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedHour.setStatus('current')
if mibBuilder.loadTexts: schedHour.setDescription('The set of hours within a day during which the scheduled action should take place. Note that implementations which maintain a list of pending activations must re-calculate them when this object is changed.')
schedMinute = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 9), Bits().clone(namedValues=NamedValues(("m0", 0), ("m1", 1), ("m2", 2), ("m3", 3), ("m4", 4), ("m5", 5), ("m6", 6), ("m7", 7), ("m8", 8), ("m9", 9), ("m10", 10), ("m11", 11), ("m12", 12), ("m13", 13), ("m14", 14), ("m15", 15), ("m16", 16), ("m17", 17), ("m18", 18), ("m19", 19), ("m20", 20), ("m21", 21), ("m22", 22), ("m23", 23), ("m24", 24), ("m25", 25), ("m26", 26), ("m27", 27), ("m28", 28), ("m29", 29), ("m30", 30), ("m31", 31), ("m32", 32), ("m33", 33), ("m34", 34), ("m35", 35), ("m36", 36), ("m37", 37), ("m38", 38), ("m39", 39), ("m40", 40), ("m41", 41), ("m42", 42), ("m43", 43), ("m44", 44), ("m45", 45), ("m46", 46), ("m47", 47), ("m48", 48), ("m49", 49), ("m50", 50), ("m51", 51), ("m52", 52), ("m53", 53), ("m54", 54), ("m55", 55), ("m56", 56), ("m57", 57), ("m58", 58), ("m59", 59)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedMinute.setStatus('current')
if mibBuilder.loadTexts: schedMinute.setDescription('The set of minutes within an hour when the scheduled action should take place. Note that implementations which maintain a list of pending activations must re-calculate them when this object is changed.')
schedContextName = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedContextName.setStatus('current')
if mibBuilder.loadTexts: schedContextName.setDescription('The context which contains the local MIB variable pointed to by schedVariable.')
schedVariable = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 11), VariablePointer().clone((0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedVariable.setStatus('current')
if mibBuilder.loadTexts: schedVariable.setDescription('An object identifier pointing to a local MIB variable which resolves to an ASN.1 primitive type of INTEGER.')
schedValue = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 12), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedValue.setStatus('current')
if mibBuilder.loadTexts: schedValue.setDescription('The value which is written to the MIB object pointed to by schedVariable when the scheduler invokes an action. The implementation shall enforce the use of access control rules when performing the set operation on schedVariable. This is accomplished by calling the isAccessAllowed abstract service interface as defined in RFC 2571. Note that an implementation may choose to issue an SNMP Set message to the SNMP engine and leave the access control decision to the normal message processing procedure.')
schedType = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("periodic", 1), ("calendar", 2), ("oneshot", 3))).clone('periodic')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedType.setStatus('current')
if mibBuilder.loadTexts: schedType.setDescription("The type of this schedule. The value periodic(1) indicates that this entry specifies a periodic schedule. A periodic schedule is defined by the value of schedInterval. The values of schedWeekDay, schedMonth, schedDay, schedHour and schedMinute are ignored. The value calendar(2) indicates that this entry describes a calendar schedule. A calendar schedule is defined by the values of schedWeekDay, schedMonth, schedDay, schedHour and schedMinute. The value of schedInterval is ignored. A calendar schedule will trigger on all local times that satisfy the bits set in schedWeekDay, schedMonth, schedDay, schedHour and schedMinute. The value oneshot(3) indicates that this entry describes a one-shot schedule. A one-shot schedule is similar to a calendar schedule with the additional feature that it disables itself by changing in the `finished' schedOperStatus once the schedule triggers an action. Note that implementations which maintain a list of pending activations must re-calculate them when this object is changed.")
schedAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedAdminStatus.setStatus('current')
if mibBuilder.loadTexts: schedAdminStatus.setDescription('The desired state of the schedule.')
schedOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("finished", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedOperStatus.setStatus('current')
if mibBuilder.loadTexts: schedOperStatus.setDescription('The current operational state of this schedule. The state enabled(1) indicates this entry is active and that the scheduler will invoke actions at appropriate times. The disabled(2) state indicates that this entry is currently inactive and ignored by the scheduler. The finished(3) state indicates that the schedule has ended. Schedules in the finished(3) state are ignored by the scheduler. A one-shot schedule enters the finished(3) state when it deactivates itself. Note that the operational state must not be enabled(1) when the schedRowStatus is not active.')
schedFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedFailures.setStatus('current')
if mibBuilder.loadTexts: schedFailures.setDescription('This variable counts the number of failures while invoking the scheduled action. This counter at most increments once for a triggered action.')
schedLastFailure = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 17), SnmpPduErrorStatus().clone('noError')).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedLastFailure.setStatus('current')
if mibBuilder.loadTexts: schedLastFailure.setDescription('The most recent error that occurred during the invocation of a scheduled action. The value noError(0) is returned if no errors have occurred yet.')
schedLastFailed = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 18), DateAndTime().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedLastFailed.setStatus('current')
if mibBuilder.loadTexts: schedLastFailed.setDescription("The date and time when the most recent failure occurred. The value '0000000000000000'H is returned if no failure occurred since the last re-initialization of the scheduler.")
schedStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 19), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedStorageType.setStatus('current')
if mibBuilder.loadTexts: schedStorageType.setDescription("This object defines whether this scheduled action is kept in volatile storage and lost upon reboot or if this row is backed up by non-volatile or permanent storage. Conceptual rows having the value `permanent' must allow write access to the columnar objects schedDescr, schedInterval, schedContextName, schedVariable, schedValue, and schedAdminStatus. If an implementation supports the schedCalendarGroup, write access must be also allowed to the columnar objects schedWeekDay, schedMonth, schedDay, schedHour, schedMinute.")
schedRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 20), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedRowStatus.setStatus('current')
if mibBuilder.loadTexts: schedRowStatus.setDescription('The status of this scheduled action. A control that allows entries to be added and removed from this table. Note that the operational state must change to enabled when the administrative state is enabled and the row status changes to active(1). Attempts to destroy(6) a row or to set a row notInService(2) while the operational state is enabled result in inconsistentValue errors. The value of this object has no effect on whether other objects in this conceptual row can be modified.')
schedTriggers = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedTriggers.setStatus('current')
if mibBuilder.loadTexts: schedTriggers.setDescription('This variable counts the number of attempts (either successful or failed) to invoke the scheduled action.')
schedTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 2, 0))
schedActionFailure = NotificationType((1, 3, 6, 1, 2, 1, 63, 2, 0, 1)).setObjects(("DISMAN-SCHEDULE-MIB", "schedLastFailure"), ("DISMAN-SCHEDULE-MIB", "schedLastFailed"))
if mibBuilder.loadTexts: schedActionFailure.setStatus('current')
if mibBuilder.loadTexts: schedActionFailure.setDescription('This notification is generated whenever the invocation of a scheduled action fails.')
schedCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 3, 1))
schedGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 3, 2))
schedCompliance2 = ModuleCompliance((1, 3, 6, 1, 2, 1, 63, 3, 1, 2)).setObjects(("DISMAN-SCHEDULE-MIB", "schedGroup2"), ("DISMAN-SCHEDULE-MIB", "schedNotificationsGroup"), ("DISMAN-SCHEDULE-MIB", "schedCalendarGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    schedCompliance2 = schedCompliance2.setStatus('current')
if mibBuilder.loadTexts: schedCompliance2.setDescription('The compliance statement for SNMP entities which implement the scheduling MIB.')
schedGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 63, 3, 2, 4)).setObjects(("DISMAN-SCHEDULE-MIB", "schedDescr"), ("DISMAN-SCHEDULE-MIB", "schedInterval"), ("DISMAN-SCHEDULE-MIB", "schedContextName"), ("DISMAN-SCHEDULE-MIB", "schedVariable"), ("DISMAN-SCHEDULE-MIB", "schedValue"), ("DISMAN-SCHEDULE-MIB", "schedType"), ("DISMAN-SCHEDULE-MIB", "schedAdminStatus"), ("DISMAN-SCHEDULE-MIB", "schedOperStatus"), ("DISMAN-SCHEDULE-MIB", "schedFailures"), ("DISMAN-SCHEDULE-MIB", "schedLastFailure"), ("DISMAN-SCHEDULE-MIB", "schedLastFailed"), ("DISMAN-SCHEDULE-MIB", "schedStorageType"), ("DISMAN-SCHEDULE-MIB", "schedRowStatus"), ("DISMAN-SCHEDULE-MIB", "schedTriggers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    schedGroup2 = schedGroup2.setStatus('current')
if mibBuilder.loadTexts: schedGroup2.setDescription('A collection of objects providing scheduling capabilities.')
schedCalendarGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 63, 3, 2, 2)).setObjects(("DISMAN-SCHEDULE-MIB", "schedLocalTime"), ("DISMAN-SCHEDULE-MIB", "schedWeekDay"), ("DISMAN-SCHEDULE-MIB", "schedMonth"), ("DISMAN-SCHEDULE-MIB", "schedDay"), ("DISMAN-SCHEDULE-MIB", "schedHour"), ("DISMAN-SCHEDULE-MIB", "schedMinute"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    schedCalendarGroup = schedCalendarGroup.setStatus('current')
if mibBuilder.loadTexts: schedCalendarGroup.setDescription('A collection of objects providing calendar based schedules.')
schedNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 63, 3, 2, 3)).setObjects(("DISMAN-SCHEDULE-MIB", "schedActionFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    schedNotificationsGroup = schedNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: schedNotificationsGroup.setDescription('The notifications emitted by the scheduler.')
schedCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 63, 3, 1, 1)).setObjects(("DISMAN-SCHEDULE-MIB", "schedGroup"), ("DISMAN-SCHEDULE-MIB", "schedNotificationsGroup"), ("DISMAN-SCHEDULE-MIB", "schedCalendarGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    schedCompliance = schedCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: schedCompliance.setDescription('The compliance statement for SNMP entities which implement the scheduling MIB.')
schedGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 63, 3, 2, 1)).setObjects(("DISMAN-SCHEDULE-MIB", "schedDescr"), ("DISMAN-SCHEDULE-MIB", "schedInterval"), ("DISMAN-SCHEDULE-MIB", "schedContextName"), ("DISMAN-SCHEDULE-MIB", "schedVariable"), ("DISMAN-SCHEDULE-MIB", "schedValue"), ("DISMAN-SCHEDULE-MIB", "schedType"), ("DISMAN-SCHEDULE-MIB", "schedAdminStatus"), ("DISMAN-SCHEDULE-MIB", "schedOperStatus"), ("DISMAN-SCHEDULE-MIB", "schedFailures"), ("DISMAN-SCHEDULE-MIB", "schedLastFailure"), ("DISMAN-SCHEDULE-MIB", "schedLastFailed"), ("DISMAN-SCHEDULE-MIB", "schedStorageType"), ("DISMAN-SCHEDULE-MIB", "schedRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    schedGroup = schedGroup.setStatus('deprecated')
if mibBuilder.loadTexts: schedGroup.setDescription('A collection of objects providing scheduling capabilities.')
mibBuilder.exportSymbols("DISMAN-SCHEDULE-MIB", schedNotifications=schedNotifications, schedMonth=schedMonth, schedLocalTime=schedLocalTime, schedMIB=schedMIB, schedGroup2=schedGroup2, schedName=schedName, schedEntry=schedEntry, schedDescr=schedDescr, schedActionFailure=schedActionFailure, schedRowStatus=schedRowStatus, schedContextName=schedContextName, schedType=schedType, schedAdminStatus=schedAdminStatus, SnmpPduErrorStatus=SnmpPduErrorStatus, schedCompliances=schedCompliances, schedGroups=schedGroups, schedHour=schedHour, schedLastFailure=schedLastFailure, schedTraps=schedTraps, schedTriggers=schedTriggers, schedFailures=schedFailures, schedNotificationsGroup=schedNotificationsGroup, schedOwner=schedOwner, schedVariable=schedVariable, schedObjects=schedObjects, schedDay=schedDay, schedValue=schedValue, schedCompliance2=schedCompliance2, schedStorageType=schedStorageType, schedMinute=schedMinute, schedGroup=schedGroup, schedCompliance=schedCompliance, schedOperStatus=schedOperStatus, schedCalendarGroup=schedCalendarGroup, schedWeekDay=schedWeekDay, schedInterval=schedInterval, schedTable=schedTable, schedLastFailed=schedLastFailed, schedConformance=schedConformance, PYSNMP_MODULE_ID=schedMIB)