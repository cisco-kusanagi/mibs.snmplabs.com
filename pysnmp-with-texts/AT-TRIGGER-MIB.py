#
# PySNMP MIB module AT-TRIGGER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-TRIGGER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:30:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, iso, IpAddress, ObjectIdentity, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, Gauge32, Unsigned32, MibIdentifier, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "IpAddress", "ObjectIdentity", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "Gauge32", "Unsigned32", "MibIdentifier", "TimeTicks", "Counter32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
trigger = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53))
trigger.setRevisions(('2010-09-07 00:00', '2010-06-15 00:15', '2007-11-28 16:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: trigger.setRevisionsDescriptions(('Generic syntax tidy up', 'MIB revision history dates in descriptions updated.', 'Added trigger configuration details for AW+',))
if mibBuilder.loadTexts: trigger.setLastUpdated('201009070000Z')
if mibBuilder.loadTexts: trigger.setOrganization('Allied Telesis, Inc')
if mibBuilder.loadTexts: trigger.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: trigger.setDescription('This MIB file contains definitions of managed objects for the TRIGGER module. ')
triggerTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 0))
triggerTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 0, 1)).setObjects(("AT-TRIGGER-MIB", "triggerLastTriggerActivated"))
if mibBuilder.loadTexts: triggerTrap.setStatus('current')
if mibBuilder.loadTexts: triggerTrap.setDescription('A trigger trap is generated a trigger is activated. The number of the trigger activated is given by the variable triggerLastTriggerActivated.')
triggerLastTriggerActivated = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerLastTriggerActivated.setStatus('current')
if mibBuilder.loadTexts: triggerLastTriggerActivated.setDescription('The trigger number of the most recent trigger activated on this router. This is also the variable sent in the trigger trap below. If no triggers have been activated yet since the last restart of this router, this variable will read as 0.')
triggerConfigInfoTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9), )
if mibBuilder.loadTexts: triggerConfigInfoTable.setStatus('current')
if mibBuilder.loadTexts: triggerConfigInfoTable.setDescription('The (conceptual) table listing entries of trigger configuration details.')
triggerConfigInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1), ).setIndexNames((0, "AT-TRIGGER-MIB", "triggerNumber"))
if mibBuilder.loadTexts: triggerConfigInfoEntry.setStatus('current')
if mibBuilder.loadTexts: triggerConfigInfoEntry.setDescription('An entry (conceptual row) in the triggerConfigInfoTable.')
triggerNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 250))).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumber.setStatus('current')
if mibBuilder.loadTexts: triggerNumber.setDescription('The object represents the ID number of the trigger.')
triggerName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerName.setStatus('current')
if mibBuilder.loadTexts: triggerName.setDescription('This object represents the name and description of the trigger.')
triggerTypeDetail = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerTypeDetail.setStatus('current')
if mibBuilder.loadTexts: triggerTypeDetail.setDescription('This object indicates the trigger type and its activation conditions.')
triggerActiveDaysOrDate = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerActiveDaysOrDate.setStatus('current')
if mibBuilder.loadTexts: triggerActiveDaysOrDate.setDescription('This objects indicates either the days of a week or the date, on which the trigger is permitted to activate.')
triggerActivateAfter = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerActivateAfter.setStatus('current')
if mibBuilder.loadTexts: triggerActivateAfter.setDescription('This object indicates the time when the trigger will be activated afterwards.')
triggerActivateBefore = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerActivateBefore.setStatus('current')
if mibBuilder.loadTexts: triggerActivateBefore.setDescription('This object indicates the time when the trigger will be activated before.')
triggerActiveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerActiveStatus.setStatus('current')
if mibBuilder.loadTexts: triggerActiveStatus.setDescription('This object indicates whether or not the trigger is permitted to activate. ')
triggerTestMode = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerTestMode.setStatus('current')
if mibBuilder.loadTexts: triggerTestMode.setDescription('This object indicates whether or not the trigger is operating in diagnostic mode. ')
triggerSnmpTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerSnmpTrap.setStatus('current')
if mibBuilder.loadTexts: triggerSnmpTrap.setDescription('This object indicates whether or not a snmp trap will be sent when the trigger is activated.')
triggerRepeatTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerRepeatTimes.setStatus('current')
if mibBuilder.loadTexts: triggerRepeatTimes.setDescription('This objects indicates whether the trigger repeats an unlimited number of times (continuous) or for a set of times. When the trigger can repeat only a set of times, then the number of times the trigger has been activated is displayed in brackets.')
triggerLasttimeModified = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerLasttimeModified.setStatus('current')
if mibBuilder.loadTexts: triggerLasttimeModified.setDescription('This object indicates the date and time of the last time that the trigger was modified.')
triggerNumberOfActivation = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumberOfActivation.setStatus('current')
if mibBuilder.loadTexts: triggerNumberOfActivation.setDescription('The objects represents the number of times the trigger has been activated since the last restart of the device. ')
triggerLasttimeActivation = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerLasttimeActivation.setStatus('current')
if mibBuilder.loadTexts: triggerLasttimeActivation.setDescription('This object indicates the date and time of the last time that the trigger was activated.')
triggerNumberOfScripts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumberOfScripts.setStatus('current')
if mibBuilder.loadTexts: triggerNumberOfScripts.setDescription('This objects represents the number of scripts that are associated with this trigger.')
triggerScript1 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerScript1.setStatus('current')
if mibBuilder.loadTexts: triggerScript1.setDescription('This objects represents the name of the 1st script that is associated with the trigger. ')
triggerScript2 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerScript2.setStatus('current')
if mibBuilder.loadTexts: triggerScript2.setDescription('This objects represents the name of the 2nd script that is associated with the trigger. ')
triggerScript3 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerScript3.setStatus('current')
if mibBuilder.loadTexts: triggerScript3.setDescription('This objects represents the name of the 3rd script that is associated with the trigger. ')
triggerScript4 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerScript4.setStatus('current')
if mibBuilder.loadTexts: triggerScript4.setDescription('This objects represents the name of the 4th script that is associated with the trigger. ')
triggerScript5 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerScript5.setStatus('current')
if mibBuilder.loadTexts: triggerScript5.setDescription('This objects represents the name of the 5th script that is associated with the trigger. ')
triggerCounters = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10))
triggerNumOfActivation = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfActivation.setStatus('current')
if mibBuilder.loadTexts: triggerNumOfActivation.setDescription('This objects represents the number of times a trigger has been activated.')
triggerNumOfActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfActivationToday.setStatus('current')
if mibBuilder.loadTexts: triggerNumOfActivationToday.setDescription('This objects represents the number of times a trigger has been activated today.')
triggerNumOfPerodicActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfPerodicActivationToday.setStatus('current')
if mibBuilder.loadTexts: triggerNumOfPerodicActivationToday.setDescription('This objects represents the number of times a periodic trigger has been activated today.')
triggerNumOfInterfaceActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfInterfaceActivationToday.setStatus('current')
if mibBuilder.loadTexts: triggerNumOfInterfaceActivationToday.setDescription('This objects represents the number of times an interface trigger has been activated today.')
triggerNumOfResourceActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfResourceActivationToday.setStatus('current')
if mibBuilder.loadTexts: triggerNumOfResourceActivationToday.setDescription('This objects represents the number of times a CPU or memory trigger has been activated today.')
triggerNumOfRebootActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfRebootActivationToday.setStatus('current')
if mibBuilder.loadTexts: triggerNumOfRebootActivationToday.setDescription('This objects represents the number of times a reboot trigger has been activated today.')
triggerNumOfPingPollActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfPingPollActivationToday.setStatus('current')
if mibBuilder.loadTexts: triggerNumOfPingPollActivationToday.setDescription('This objects represents the number of times a ping-poll trigger has been activated today.')
triggerNumOfStackMasterFailActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfStackMasterFailActivationToday.setStatus('current')
if mibBuilder.loadTexts: triggerNumOfStackMasterFailActivationToday.setDescription('This objects represents the number of times a stack master fail trigger has been activated today.')
triggerNumOfStackMemberActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfStackMemberActivationToday.setStatus('current')
if mibBuilder.loadTexts: triggerNumOfStackMemberActivationToday.setDescription('This objects represents the number of times a stack member trigger has been activated today.')
triggerNumOfStackXemStkActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfStackXemStkActivationToday.setStatus('current')
if mibBuilder.loadTexts: triggerNumOfStackXemStkActivationToday.setDescription('This objects represents the number of times a stack xem-stack trigger has been activated today.')
mibBuilder.exportSymbols("AT-TRIGGER-MIB", triggerScript2=triggerScript2, triggerLasttimeActivation=triggerLasttimeActivation, triggerNumOfStackMasterFailActivationToday=triggerNumOfStackMasterFailActivationToday, triggerNumOfInterfaceActivationToday=triggerNumOfInterfaceActivationToday, triggerActiveStatus=triggerActiveStatus, triggerTraps=triggerTraps, triggerConfigInfoEntry=triggerConfigInfoEntry, triggerNumberOfActivation=triggerNumberOfActivation, triggerActivateBefore=triggerActivateBefore, triggerNumOfResourceActivationToday=triggerNumOfResourceActivationToday, PYSNMP_MODULE_ID=trigger, triggerTrap=triggerTrap, triggerConfigInfoTable=triggerConfigInfoTable, trigger=trigger, triggerNumOfRebootActivationToday=triggerNumOfRebootActivationToday, triggerName=triggerName, triggerNumberOfScripts=triggerNumberOfScripts, triggerNumOfActivation=triggerNumOfActivation, triggerLastTriggerActivated=triggerLastTriggerActivated, triggerNumOfStackXemStkActivationToday=triggerNumOfStackXemStkActivationToday, triggerTestMode=triggerTestMode, triggerTypeDetail=triggerTypeDetail, triggerActiveDaysOrDate=triggerActiveDaysOrDate, triggerScript3=triggerScript3, triggerCounters=triggerCounters, triggerRepeatTimes=triggerRepeatTimes, triggerScript4=triggerScript4, triggerSnmpTrap=triggerSnmpTrap, triggerNumOfPingPollActivationToday=triggerNumOfPingPollActivationToday, triggerNumOfStackMemberActivationToday=triggerNumOfStackMemberActivationToday, triggerNumber=triggerNumber, triggerNumOfActivationToday=triggerNumOfActivationToday, triggerLasttimeModified=triggerLasttimeModified, triggerScript5=triggerScript5, triggerNumOfPerodicActivationToday=triggerNumOfPerodicActivationToday, triggerScript1=triggerScript1, triggerActivateAfter=triggerActivateAfter)
