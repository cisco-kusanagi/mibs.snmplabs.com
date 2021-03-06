#
# PySNMP MIB module MOXA-IO-E1242-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MOXA-IO-E1242-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:13:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, Unsigned32, Counter32, Counter64, IpAddress, iso, TimeTicks, Integer32, MibIdentifier, enterprises, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "Unsigned32", "Counter32", "Counter64", "IpAddress", "iso", "TimeTicks", "Integer32", "MibIdentifier", "enterprises", "Bits", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
e1242 = ModuleIdentity((1, 3, 6, 1, 4, 1, 8691, 10, 1242))
e1242.setRevisions(('2013-02-21 14:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: e1242.setRevisionsDescriptions(('First version of this MIB.',))
if mibBuilder.loadTexts: e1242.setLastUpdated('201302211400Z')
if mibBuilder.loadTexts: e1242.setOrganization('Moxa Automation,Inc.')
if mibBuilder.loadTexts: e1242.setContactInfo('Postal: Moxa Automation,Inc. Fl.4, No.135,Lane 235,Pao-Chiao Rd. Shing Tien City,Taipei,Taiwan,R.O.C Tel: +866-2-89191230 ')
if mibBuilder.loadTexts: e1242.setDescription('The MIB module for Moxa ioLogik Remote Ethernet I/O specific information.')
moxa = MibIdentifier((1, 3, 6, 1, 4, 1, 8691))
ioLogik = MibIdentifier((1, 3, 6, 1, 4, 1, 8691, 10))
totalChannelNumber = MibScalar((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalChannelNumber.setStatus('current')
if mibBuilder.loadTexts: totalChannelNumber.setDescription('Total I/O channels.')
serverModel = MibScalar((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverModel.setStatus('current')
if mibBuilder.loadTexts: serverModel.setDescription('The I/O server model.')
systemTime = MibScalar((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemTime.setStatus('current')
if mibBuilder.loadTexts: systemTime.setDescription('I/O server up time (in seconds).')
firmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firmwareVersion.setStatus('current')
if mibBuilder.loadTexts: firmwareVersion.setDescription('The firmware version.')
e1242monitor = MibIdentifier((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10))
diTable = MibTable((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 1), )
if mibBuilder.loadTexts: diTable.setStatus('current')
if mibBuilder.loadTexts: diTable.setDescription('The DI channel monitor table')
diEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 1, 1), ).setIndexNames((0, "MOXA-IO-E1242-MIB", "diIndex"))
if mibBuilder.loadTexts: diEntry.setStatus('current')
if mibBuilder.loadTexts: diEntry.setDescription('The DI channel monitor item')
diIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diIndex.setStatus('current')
if mibBuilder.loadTexts: diIndex.setDescription('The channel DI index.')
diType = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diType.setStatus('current')
if mibBuilder.loadTexts: diType.setDescription('The channel DI type. 0=DI, 1=DO')
diMode = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diMode.setStatus('current')
if mibBuilder.loadTexts: diMode.setDescription('The channel DI mode. 0=DI, 1=Event Counter')
diStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diStatus.setStatus('current')
if mibBuilder.loadTexts: diStatus.setDescription('The channel DI status. 0=Off, 1=On in DI mode or N=Count in counter mode')
diFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diFilter.setStatus('current')
if mibBuilder.loadTexts: diFilter.setDescription('The channel DI counter filter. unit=1ms')
diTrigger = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diTrigger.setStatus('current')
if mibBuilder.loadTexts: diTrigger.setDescription('The channel DI counter trigger level. 0=L2H, 1=H2L, 2=Both')
diCntStart = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diCntStart.setStatus('current')
if mibBuilder.loadTexts: diCntStart.setDescription('The channel DI counter start/stop. 0=stop, 1=start')
dioTable = MibTable((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3), )
if mibBuilder.loadTexts: dioTable.setStatus('current')
if mibBuilder.loadTexts: dioTable.setDescription('The DIO channel monitor table')
dioEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3, 1), ).setIndexNames((0, "MOXA-IO-E1242-MIB", "dioIndex"))
if mibBuilder.loadTexts: dioEntry.setStatus('current')
if mibBuilder.loadTexts: dioEntry.setDescription('The DIO channel monitor item')
dioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dioIndex.setStatus('current')
if mibBuilder.loadTexts: dioIndex.setDescription('The channel DI/DO index.')
dioType = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dioType.setStatus('current')
if mibBuilder.loadTexts: dioType.setDescription('The channel DIO type. 0=DI, DO=1')
dioMode = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dioMode.setStatus('current')
if mibBuilder.loadTexts: dioMode.setDescription('The channel DI Type(0=DI, 1=Event Counter),DO Type(0=DO, 1=Pulse Output).')
dioStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dioStatus.setStatus('current')
if mibBuilder.loadTexts: dioStatus.setDescription('The channel DI status.(0=Off, 1=On in DI mode or N=Count in counter mode),DO status(0=Off, 1=On in DO mode or N=Count in pulse mode)')
dioDIFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dioDIFilter.setStatus('current')
if mibBuilder.loadTexts: dioDIFilter.setDescription('The channel DI counter filter. unit=1ms')
dioDITrigger = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dioDITrigger.setStatus('current')
if mibBuilder.loadTexts: dioDITrigger.setDescription('The channel DI counter trigger level. 0=L2H, 1=H2L, 2=Both')
dioDICntStart = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dioDICntStart.setStatus('current')
if mibBuilder.loadTexts: dioDICntStart.setDescription('The channel DI counter start/stop. 0=stop, 1=start')
dioDOPulsONWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dioDOPulsONWidth.setStatus('current')
if mibBuilder.loadTexts: dioDOPulsONWidth.setDescription('The channel DO signal ON width. unit=1ms')
dioDOPulsOFFWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dioDOPulsOFFWidth.setStatus('current')
if mibBuilder.loadTexts: dioDOPulsOFFWidth.setDescription('The channel DO signal OFF width. unit=1ms')
dioDOPulseStart = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dioDOPulseStart.setStatus('current')
if mibBuilder.loadTexts: dioDOPulseStart.setDescription('The channel DO pulse start/stop. 0=stop, 1=start')
aiTable = MibTable((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 4), )
if mibBuilder.loadTexts: aiTable.setStatus('current')
if mibBuilder.loadTexts: aiTable.setDescription('The ai channel monitor table')
aiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 4, 1), ).setIndexNames((0, "MOXA-IO-E1242-MIB", "aiIndex"))
if mibBuilder.loadTexts: aiEntry.setStatus('current')
if mibBuilder.loadTexts: aiEntry.setDescription('The ai channel monitor item')
aiIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiIndex.setStatus('current')
if mibBuilder.loadTexts: aiIndex.setDescription('The ai channel index.')
aiEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiEnable.setStatus('current')
if mibBuilder.loadTexts: aiEnable.setDescription('The ai channel Enable/Disable. Disable=0, Enable=1')
aiMode = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiMode.setStatus('current')
if mibBuilder.loadTexts: aiMode.setDescription('The ai channel Mode. 0-10V=0, 4-20mA=1, 0-20mA=2, 4-20mA Burnout=4')
aiValue = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiValue.setStatus('current')
if mibBuilder.loadTexts: aiValue.setDescription('The ai channel value (RAW).')
aiMin = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiMin.setStatus('current')
if mibBuilder.loadTexts: aiMin.setDescription('The ai channel minimum value (RAW).')
aiMax = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiMax.setStatus('current')
if mibBuilder.loadTexts: aiMax.setDescription('The ai channel maximum value (RAW).')
aiTrap_Greater = MibIdentifier((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 22))
aiTrapG0 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 22) + (0,1))
if mibBuilder.loadTexts: aiTrapG0.setDescription('The ai channel-00 Greater Trap.')
aiTrapG1 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 22) + (0,2))
if mibBuilder.loadTexts: aiTrapG1.setDescription('The ai channel-01 Greater Trap.')
aiTrapG2 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 22) + (0,3))
if mibBuilder.loadTexts: aiTrapG2.setDescription('The ai channel-02 Greater Trap.')
aiTrapG3 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 22) + (0,4))
if mibBuilder.loadTexts: aiTrapG3.setDescription('The ai channel-03 Greater Trap.')
aiTrap_Smaller = MibIdentifier((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 23))
aiTrapS0 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 23) + (0,1))
if mibBuilder.loadTexts: aiTrapS0.setDescription('The ai channel-00 Smaller Trap.')
aiTrapS1 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 23) + (0,2))
if mibBuilder.loadTexts: aiTrapS1.setDescription('The ai channel-01 Smaller Trap.')
aiTrapS2 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 23) + (0,3))
if mibBuilder.loadTexts: aiTrapS2.setDescription('The ai channel-02 Smaller Trap.')
aiTrapS3 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 23) + (0,4))
if mibBuilder.loadTexts: aiTrapS3.setDescription('The ai channel-03 Smaller Trap.')
messageTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 30))
activeMessageTrap = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 1242, 30) + (0,1))
if mibBuilder.loadTexts: activeMessageTrap.setDescription('The SNMP trap with active message')
mibBuilder.exportSymbols("MOXA-IO-E1242-MIB", dioDOPulsOFFWidth=dioDOPulsOFFWidth, dioDICntStart=dioDICntStart, diType=diType, diFilter=diFilter, diIndex=diIndex, dioEntry=dioEntry, totalChannelNumber=totalChannelNumber, aiTrapG2=aiTrapG2, dioDIFilter=dioDIFilter, aiTrapS0=aiTrapS0, aiMode=aiMode, dioType=dioType, serverModel=serverModel, aiTrap_Smaller=aiTrap_Smaller, diTrigger=diTrigger, dioDITrigger=dioDITrigger, dioIndex=dioIndex, dioDOPulsONWidth=dioDOPulsONWidth, aiMax=aiMax, ioLogik=ioLogik, dioTable=dioTable, diCntStart=diCntStart, e1242=e1242, aiValue=aiValue, systemTime=systemTime, aiTrapS3=aiTrapS3, aiTrapS2=aiTrapS2, aiEnable=aiEnable, moxa=moxa, firmwareVersion=firmwareVersion, aiTrapS1=aiTrapS1, aiMin=aiMin, e1242monitor=e1242monitor, aiIndex=aiIndex, activeMessageTrap=activeMessageTrap, aiEntry=aiEntry, aiTrap_Greater=aiTrap_Greater, diEntry=diEntry, PYSNMP_MODULE_ID=e1242, diTable=diTable, diMode=diMode, aiTrapG1=aiTrapG1, dioDOPulseStart=dioDOPulseStart, aiTrapG3=aiTrapG3, aiTrapG0=aiTrapG0, dioMode=dioMode, dioStatus=dioStatus, diStatus=diStatus, messageTrap=messageTrap, aiTable=aiTable)
