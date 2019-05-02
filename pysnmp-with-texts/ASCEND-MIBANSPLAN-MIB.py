#
# PySNMP MIB module ASCEND-MIBANSPLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBANSPLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:26:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, ModuleIdentity, TimeTicks, ObjectIdentity, IpAddress, Integer32, NotificationType, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "IpAddress", "Integer32", "NotificationType", "Counter64", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibanswerPlanProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 34))
mibanswerPlanProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 34, 1), )
if mibBuilder.loadTexts: mibanswerPlanProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibanswerPlanProfileTable.setDescription('A list of mibanswerPlanProfile profile entries.')
mibanswerPlanProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 34, 1, 1), ).setIndexNames((0, "ASCEND-MIBANSPLAN-MIB", "answerPlanProfile-Name"))
if mibBuilder.loadTexts: mibanswerPlanProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibanswerPlanProfileEntry.setDescription('A mibanswerPlanProfile entry containing objects that maps to the parameters of mibanswerPlanProfile profile.')
answerPlanProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 34, 1, 1, 1), DisplayString()).setLabel("answerPlanProfile-Name").setMaxAccess("readonly")
if mibBuilder.loadTexts: answerPlanProfile_Name.setStatus('mandatory')
if mibBuilder.loadTexts: answerPlanProfile_Name.setDescription('')
answerPlanProfile_AnswerNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 34, 1, 1, 2), DisplayString()).setLabel("answerPlanProfile-AnswerNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: answerPlanProfile_AnswerNumber.setStatus('mandatory')
if mibBuilder.loadTexts: answerPlanProfile_AnswerNumber.setDescription('Phone number to match when routing by incoming phone number.')
answerPlanProfile_AnswerCallType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 34, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 255, 263))).clone(namedValues=NamedValues(("voice", 1), ("n-56kRestricted", 2), ("n-64kClear", 3), ("n-64kRestricted", 4), ("n-56kClear", 5), ("n-384kRestricted", 6), ("n-384kClear", 7), ("n-1536kClear", 8), ("n-1536kRestricted", 9), ("n-128kClear", 10), ("n-192kClear", 11), ("n-256kClear", 12), ("n-320kClear", 13), ("dws384Clear", 14), ("n-448Clear", 15), ("n-512Clear", 16), ("n-576Clear", 17), ("n-640Clear", 18), ("n-704Clear", 19), ("n-768Clear", 20), ("n-832Clear", 21), ("n-896Clear", 22), ("n-960Clear", 23), ("n-1024Clear", 24), ("n-1088Clear", 25), ("n-1152Clear", 26), ("n-1216Clear", 27), ("n-1280Clear", 28), ("n-1344Clear", 29), ("n-1408Clear", 30), ("n-1472Clear", 31), ("n-1600Clear", 32), ("n-1664Clear", 33), ("n-1728Clear", 34), ("n-1792Clear", 35), ("n-1856Clear", 36), ("n-1920Clear", 37), ("x30RestrictedBearer", 39), ("v110ClearBearer", 40), ("n-64kX30Restricted", 41), ("n-56kV110Clear", 42), ("modem", 43), ("atmodem", 44), ("n-2456kV110", 46), ("n-4856kV110", 47), ("n-9656kV110", 48), ("n-19256kV110", 49), ("n-38456kV110", 50), ("n-2456krV110", 51), ("n-4856krV110", 52), ("n-9656krV110", 53), ("n-19256krV110", 54), ("n-38456krV110", 55), ("n-2464kV110", 56), ("n-4864kV110", 57), ("n-9664kV110", 58), ("n-19264kV110", 59), ("n-38464kV110", 60), ("n-2464krV110", 61), ("n-4864krV110", 62), ("n-9664krV110", 63), ("n-19264krV110", 64), ("n-38464krV110", 65), ("v32", 66), ("phs64k", 67), ("voiceOverIp", 68), ("atmSvc", 70), ("frameRelaySvc", 71), ("vpnTunnel", 72), ("wormarq", 73), ("n-14456kV110", 74), ("n-28856kV110", 75), ("n-14456krV110", 76), ("n-28856krV110", 77), ("n-14464kV110", 78), ("n-28864kV110", 79), ("n-14464krV110", 80), ("n-28864krV110", 81), ("modem31khzAudio", 82), ("x25Svc", 83), ("n-144kClear", 255), ("iptoip", 263)))).setLabel("answerPlanProfile-AnswerCallType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: answerPlanProfile_AnswerCallType.setStatus('mandatory')
if mibBuilder.loadTexts: answerPlanProfile_AnswerCallType.setDescription('The switched call type (or any) that is used to map a network call to a destChanGroup.')
answerPlanProfile_DestChanGroup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 34, 1, 1, 4), Integer32()).setLabel("answerPlanProfile-DestChanGroup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: answerPlanProfile_DestChanGroup.setStatus('mandatory')
if mibBuilder.loadTexts: answerPlanProfile_DestChanGroup.setDescription('A number that identifies the channel-group to which incoming calls that match these criteria will be directed.')
answerPlanProfile_DialPlanNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 34, 1, 1, 5), Integer32()).setLabel("answerPlanProfile-DialPlanNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: answerPlanProfile_DialPlanNumber.setStatus('mandatory')
if mibBuilder.loadTexts: answerPlanProfile_DialPlanNumber.setDescription('A number that identifies the dial plan from the dial plan menu. Priority: net/t1(dialPlan#, Select-Digits), answerPlan(dialPlan#)')
answerPlanProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 34, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("answerPlanProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: answerPlanProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: answerPlanProfile_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBANSPLAN-MIB", answerPlanProfile_Action_o=answerPlanProfile_Action_o, answerPlanProfile_DestChanGroup=answerPlanProfile_DestChanGroup, mibanswerPlanProfileEntry=mibanswerPlanProfileEntry, mibanswerPlanProfile=mibanswerPlanProfile, answerPlanProfile_DialPlanNumber=answerPlanProfile_DialPlanNumber, answerPlanProfile_AnswerNumber=answerPlanProfile_AnswerNumber, answerPlanProfile_AnswerCallType=answerPlanProfile_AnswerCallType, answerPlanProfile_Name=answerPlanProfile_Name, DisplayString=DisplayString, mibanswerPlanProfileTable=mibanswerPlanProfileTable)
