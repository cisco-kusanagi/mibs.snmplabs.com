#
# PySNMP MIB module SONOMASYSTEMS-SONOMA-TRNCPQ-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONOMASYSTEMS-SONOMA-TRNCPQ-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:09:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, NotificationType, Unsigned32, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, Integer32, Counter64, Counter32, TimeTicks, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Unsigned32", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "Integer32", "Counter64", "Counter32", "TimeTicks", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sonomaLAN, = mibBuilder.importSymbols("SONOMASYSTEMS-SONOMA-MIB", "sonomaLAN")
class PhysAddress(OctetString):
    pass

sonomaTokenRing = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2))
tokenRingAdapterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1))
trnCpqGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1))
trnCpqAdapterTable = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 1), )
if mibBuilder.loadTexts: trnCpqAdapterTable.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqAdapterTable.setDescription('This table contains the configuration and status information for the Token Ring 4/16 adapter cards.')
trnCpqAdapterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 1, 1), ).setIndexNames((0, "SONOMASYSTEMS-SONOMA-TRNCPQ-MIB", "trnCpqAdapterIndex"))
if mibBuilder.loadTexts: trnCpqAdapterEntry.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqAdapterEntry.setDescription('An entry in the table of configuration and status information for the Token Ring 4/16 adapter cards.')
trnCpqAdapterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqAdapterIndex.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqAdapterIndex.setDescription('The adapter number which identifies the instance of this adapter in the Sonoma system.')
trnCpqAdapterCheckState = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))).clone(namedValues=NamedValues(("noErrors", 1), ("adapterParity", 2), ("illegalOpCode", 3), ("arithmeticFault", 4), ("illegalMAC", 5), ("dioParity", 6), ("dmaParity", 7), ("dmaBus", 8), ("dmaTimeout", 9), ("unknown", 10), ("invalidXOP", 11), ("invalidINTR", 12), ("registerParity", 13), ("ramFailure", 14), ("phtxHalt", 15), ("phtxRun", 16), ("adapterOutput", 17), ("adapterProcessComplete", 18)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqAdapterCheckState.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqAdapterCheckState.setDescription('This object signifies the adapter check information when the AdapterCheck Interrupt has occured and the adapter is in a closed state waiting to be reset.')
trnCpqAdapterOpenInWrapMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trnCpqAdapterOpenInWrapMode.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqAdapterOpenInWrapMode.setDescription('This enables the adapter to open in Wrap Mode. In order to set/reset this parameter, close the logical port, change the value and open the port.')
trnCpqAdapterEarlyTokenRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trnCpqAdapterEarlyTokenRelease.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqAdapterEarlyTokenRelease.setDescription('This enables the early token release . In order to set/reset this parameter, close the logical port, change the value and open the port.')
trnCpqAdapterGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 1, 1, 5), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trnCpqAdapterGroupAddress.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqAdapterGroupAddress.setDescription('The Group address of the adapter.')
trnCpqRingSpeedDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("manual", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trnCpqRingSpeedDetect.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqRingSpeedDetect.setDescription('This specifies whether during open operation the card should autodetect the ring speed or read the dot5RingSpeed value and try to insert into the ring.')
trnCpqMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(256, 17952))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trnCpqMtu.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqMtu.setDescription('This specifies the mtu for the adapter. The actual packet size may be less depending on other adapters in the unit. Changes will not take affect until the next reboot.')
trnCpqAdapterCheckStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2), )
if mibBuilder.loadTexts: trnCpqAdapterCheckStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqAdapterCheckStatsTable.setDescription('A Table having Adapter Check statistics specific to the Sonoma TRNCPQ Token Ring Adapter Cards, one entry per card.')
trnCpqAdapterCheckStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1), ).setIndexNames((0, "SONOMASYSTEMS-SONOMA-TRNCPQ-MIB", "trnCpqAdapterCheckStatsIndex"))
if mibBuilder.loadTexts: trnCpqAdapterCheckStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqAdapterCheckStatsEntry.setDescription('An entry contains the sonoma token ring adapter check statistics for a particular interface.')
trnCpqAdapterCheckStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqAdapterCheckStatsIndex.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqAdapterCheckStatsIndex.setDescription('The value of this object identifies the sonoma token ring adapter interface for which this entry contains management information.')
trnCpqAdapParityErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqAdapParityErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqAdapParityErrors.setDescription("The number of times the adapter detected a bus parity error on the adapter's internal bus.")
trnCpqIllOpCodeErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqIllOpCodeErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqIllOpCodeErrors.setDescription("The number of times the adapter's communications processor detected an illegal opcode in the adapter's internal program.")
trnCpqArithFaultErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqArithFaultErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqArithFaultErrors.setDescription('The number of times there was an arithmetic fault.')
trnCpqIllMemErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqIllMemErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqIllMemErrors.setDescription('The number of illegal memory access occured.')
trnCpqDIOParityErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqDIOParityErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqDIOParityErrors.setDescription('The number of times the adapter detected a bad parity on data passed from the attached system to the adapter through a direct I/O access.')
trnCpqDMAParityErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqDMAParityErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqDMAParityErrors.setDescription('The number of times the adapter aborted a DMA operation as a result of parity errors.')
trnCpqDMABusErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqDMABusErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqDMABusErrors.setDescription('The number of times the adapter aborted a DMA operation as a result of bus errors.')
trnCpqDMATimeoutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqDMATimeoutErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqDMATimeoutErrors.setDescription('The number of times the adapter timed out waiting for the completion of a DMA operation.')
trnCpqInvIntrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqInvIntrErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqInvIntrErrors.setDescription('The number of times an unrecognized error interrupt was generated.')
trnCpqInvXOPErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqInvXOPErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqInvXOPErrors.setDescription('The number of times an unrecognized XOP request was generated in the communications processor code.')
trnCpqRegParityErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqRegParityErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqRegParityErrors.setDescription('The number of times a parity error occured in the user register.')
trnCpqRAMFailErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqRAMFailErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqRAMFailErrors.setDescription('The number of times Extended RAM failure occured.')
trnCpqPHTxHaltErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqPHTxHaltErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqPHTxHaltErrors.setDescription('The number of times DMA was unable to be stopped.')
trnCpqPHTxRunErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqPHTxRunErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqPHTxRunErrors.setDescription('The number of internal DMA underruns when transmitting onto the ring.')
trnCpqBUDStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 3), )
if mibBuilder.loadTexts: trnCpqBUDStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqBUDStatsTable.setDescription('A Table having BUD statistics specific to the Sonoma TRNCPQ Token Ring Adapter Cards, one entry per card.')
trnCpqBUDStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 3, 1), ).setIndexNames((0, "SONOMASYSTEMS-SONOMA-TRNCPQ-MIB", "trnCpqBUDStatsIndex"))
if mibBuilder.loadTexts: trnCpqBUDStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqBUDStatsEntry.setDescription('An entry contains the sonoma token ring adapter statistics for a particular interface.')
trnCpqBUDStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqBUDStatsIndex.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqBUDStatsIndex.setDescription('The value of this object identifies the sonoma token ring adapter interface for which this entry contains management information.')
trnCpqInitialTestErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqInitialTestErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqInitialTestErrors.setDescription('Initial Test error during BUD.')
trnCpqChecksumErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqChecksumErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqChecksumErrors.setDescription('Checksum errors during BUD.')
trnCpqAdapterRAMErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqAdapterRAMErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqAdapterRAMErrors.setDescription('Adapter RAM errors during BUD.')
trnCpqInstructionTestErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqInstructionTestErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqInstructionTestErrors.setDescription('Instruction Test errors during BUD.')
trnCpqCtxtorIntrTestErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqCtxtorIntrTestErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqCtxtorIntrTestErrors.setDescription('Context or Interrupt test errors during BUD.')
trnCpqProtocolHandlerHWErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqProtocolHandlerHWErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqProtocolHandlerHWErrors.setDescription('Protocol handler hardware error during BUD.')
trnCpqSystemInterfaceRegErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqSystemInterfaceRegErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqSystemInterfaceRegErrors.setDescription('System Interface register error during BUD.')
trnCpqInitStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4), )
if mibBuilder.loadTexts: trnCpqInitStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqInitStatsTable.setDescription('A Table having BUD and Initialization statistics specific to the Sonoma TRNCPQ Token Ring Adapter Cards, one entry per card.')
trnCpqInitStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1), ).setIndexNames((0, "SONOMASYSTEMS-SONOMA-TRNCPQ-MIB", "trnCpqInitStatsIndex"))
if mibBuilder.loadTexts: trnCpqInitStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqInitStatsEntry.setDescription('An entry contains the sonoma token ring adapter statistics for a particular interface.')
trnCpqInitStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqInitStatsIndex.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqInitStatsIndex.setDescription('The value of this object identifies the sonoma token ring adapter interface for which this entry contains management information.')
trnCpqInvInitBlocksErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqInvInitBlocksErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqInvInitBlocksErrors.setDescription('The number of times the initialization parameter block was not transferred in full to the adapter.')
trnCpqInvInitOptionsErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqInvInitOptionsErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqInvInitOptionsErrors.setDescription('The number of times the bit 0 was not 1 or the other bits were not 0 in the initialization parameter block.')
trnCpqNoResourcesErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqNoResourcesErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqNoResourcesErrors.setDescription('The number of times there was insufficient adapter memory for the microcode.')
trnCpqInitAddressErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqInitAddressErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqInitAddressErrors.setDescription('The number of times invalid hcb/hsb addresses caused an error during initialization.')
trnCpqInitDIOParityErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqInitDIOParityErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqInitDIOParityErrors.setDescription('The number of times the adapter detected a bad parity on data passed from the attached system to the adapter through a direct I/O access, during initialization.')
trnCpqInitDMAParityErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqInitDMAParityErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqInitDMAParityErrors.setDescription('The number of times the adapter aborted a DMA operation as a result of parity errors during initialization.')
trnCpqInitDMABusErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqInitDMABusErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqInitDMABusErrors.setDescription('The number of times the adapter aborted a DMA operation as a result of bus errors during initialization.')
trnCpqInitDMATimeoutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqInitDMATimeoutErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqInitDMATimeoutErrors.setDescription('The number of times the adapter timed out waiting for the completion of a DMA operationduring initialization.')
trnCpqInitDMADataErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqInitDMADataErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqInitDMADataErrors.setDescription('The number of times a DMA test failed because of data miscompare during initialization.')
trnCpqAdapterCheckErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqAdapterCheckErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqAdapterCheckErrors.setDescription('The number of times an unrecoverable hardware or software error occured during initialization.')
trnCpqMiscStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5), )
if mibBuilder.loadTexts: trnCpqMiscStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqMiscStatsTable.setDescription('A Table having miscellaneous statistics specific to the Sonoma TRNCPQ Token Ring Adapter Cards, one entry per card.')
trnCpqMiscStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1), ).setIndexNames((0, "SONOMASYSTEMS-SONOMA-TRNCPQ-MIB", "trnCpqMiscStatsIndex"))
if mibBuilder.loadTexts: trnCpqMiscStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqMiscStatsEntry.setDescription('An entry contains the sonoma token ring adapter statistics for a particular interface.')
trnCpqMiscStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqMiscStatsIndex.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqMiscStatsIndex.setDescription('The value of this object identifies the sonoma token ring adapter interface for which this entry contains management information.')
trnCpqCounterOverflowErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqCounterOverflowErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqCounterOverflowErrors.setDescription('The number of times the adapter error counters have incremented from 254 to 255.')
trnCpqAutoRemovalErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqAutoRemovalErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqAutoRemovalErrors.setDescription('The number of times the adapter has failed the lobe wrap test resulting from the beacon auto-removal process and has de-inserted from the ring.')
trnCpqFrameBigErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqFrameBigErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqFrameBigErrors.setDescription('The number of times a received packet was discarded because the received frame was larger than Max_Frame_Size.')
trnCpqNoHostBufErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqNoHostBufErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqNoHostBufErrors.setDescription('The number of times a received packet was discarded because there was no host buffer available in the Receive Structure Array.')
trnCpqAddressErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqAddressErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqAddressErrors.setDescription('The number of times an error occured due to invalid addresses. This does not include errors that occur during initialization. Those errors are being handled in the BUD specific table.')
trnCpqAdapNotInsertedErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqAdapNotInsertedErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqAdapNotInsertedErrors.setDescription('The number of times an operation failed because of the adapter not being inserted.')
trnCpqMiscRcvErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqMiscRcvErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqMiscRcvErrors.setDescription('The number of times a receive error was detected by the microcode.')
trnCpqNoOfLinkResets = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqNoOfLinkResets.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqNoOfLinkResets.setDescription('This object is a count of the number of resets which have occurred on this Token Ring link, since the last reinitialization of the unit.')
trnCpqLastLinkResetReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noReason", 1), ("management", 2), ("deviceError", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqLastLinkResetReason.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqLastLinkResetReason.setDescription('This object gives the a reason code for the last reset which occurred on this Token ring port. This object gives the reason code for the last reset which occurred on this LAN physical link. A value of noReason(1) is returned if the link has not reset. A value of management(2) is returned when a link reset has been caused by SNMP. A value of deviceError(3) is returned if the link reset was caused by a hardware failure.')
trnCpqTimeSinceLastLinkReset = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trnCpqTimeSinceLastLinkReset.setStatus('mandatory')
if mibBuilder.loadTexts: trnCpqTimeSinceLastLinkReset.setDescription('This object gives the time (in hundreths of seconds) since the last link reset, eg. The time since the last link went down. The value of this object is zero if no link resets have occured since the last reinitialization of the unit.')
mibBuilder.exportSymbols("SONOMASYSTEMS-SONOMA-TRNCPQ-MIB", trnCpqAdapterEarlyTokenRelease=trnCpqAdapterEarlyTokenRelease, trnCpqAdapterCheckErrors=trnCpqAdapterCheckErrors, trnCpqDMABusErrors=trnCpqDMABusErrors, trnCpqNoOfLinkResets=trnCpqNoOfLinkResets, trnCpqMiscRcvErrors=trnCpqMiscRcvErrors, trnCpqInitStatsEntry=trnCpqInitStatsEntry, trnCpqAdapterCheckState=trnCpqAdapterCheckState, trnCpqAutoRemovalErrors=trnCpqAutoRemovalErrors, trnCpqDMATimeoutErrors=trnCpqDMATimeoutErrors, trnCpqProtocolHandlerHWErrors=trnCpqProtocolHandlerHWErrors, trnCpqIllOpCodeErrors=trnCpqIllOpCodeErrors, trnCpqInvIntrErrors=trnCpqInvIntrErrors, trnCpqInitDMADataErrors=trnCpqInitDMADataErrors, trnCpqAdapNotInsertedErrors=trnCpqAdapNotInsertedErrors, trnCpqInitDIOParityErrors=trnCpqInitDIOParityErrors, trnCpqArithFaultErrors=trnCpqArithFaultErrors, trnCpqDMAParityErrors=trnCpqDMAParityErrors, trnCpqBUDStatsIndex=trnCpqBUDStatsIndex, trnCpqLastLinkResetReason=trnCpqLastLinkResetReason, trnCpqPHTxHaltErrors=trnCpqPHTxHaltErrors, trnCpqPHTxRunErrors=trnCpqPHTxRunErrors, trnCpqCounterOverflowErrors=trnCpqCounterOverflowErrors, trnCpqAdapterEntry=trnCpqAdapterEntry, trnCpqDIOParityErrors=trnCpqDIOParityErrors, trnCpqMtu=trnCpqMtu, trnCpqRAMFailErrors=trnCpqRAMFailErrors, PhysAddress=PhysAddress, trnCpqInitStatsIndex=trnCpqInitStatsIndex, trnCpqInvInitBlocksErrors=trnCpqInvInitBlocksErrors, trnCpqAdapterCheckStatsEntry=trnCpqAdapterCheckStatsEntry, trnCpqNoResourcesErrors=trnCpqNoResourcesErrors, trnCpqInvInitOptionsErrors=trnCpqInvInitOptionsErrors, trnCpqInvXOPErrors=trnCpqInvXOPErrors, trnCpqFrameBigErrors=trnCpqFrameBigErrors, trnCpqInitDMABusErrors=trnCpqInitDMABusErrors, trnCpqAdapterCheckStatsTable=trnCpqAdapterCheckStatsTable, trnCpqAdapterTable=trnCpqAdapterTable, trnCpqGroup=trnCpqGroup, trnCpqMiscStatsIndex=trnCpqMiscStatsIndex, trnCpqNoHostBufErrors=trnCpqNoHostBufErrors, trnCpqAdapterOpenInWrapMode=trnCpqAdapterOpenInWrapMode, tokenRingAdapterGroup=tokenRingAdapterGroup, trnCpqAdapParityErrors=trnCpqAdapParityErrors, trnCpqInitialTestErrors=trnCpqInitialTestErrors, trnCpqCtxtorIntrTestErrors=trnCpqCtxtorIntrTestErrors, trnCpqInitStatsTable=trnCpqInitStatsTable, trnCpqInitDMAParityErrors=trnCpqInitDMAParityErrors, trnCpqChecksumErrors=trnCpqChecksumErrors, trnCpqAdapterRAMErrors=trnCpqAdapterRAMErrors, trnCpqAddressErrors=trnCpqAddressErrors, sonomaTokenRing=sonomaTokenRing, trnCpqMiscStatsTable=trnCpqMiscStatsTable, trnCpqAdapterGroupAddress=trnCpqAdapterGroupAddress, trnCpqInstructionTestErrors=trnCpqInstructionTestErrors, trnCpqTimeSinceLastLinkReset=trnCpqTimeSinceLastLinkReset, trnCpqIllMemErrors=trnCpqIllMemErrors, trnCpqInitAddressErrors=trnCpqInitAddressErrors, trnCpqMiscStatsEntry=trnCpqMiscStatsEntry, trnCpqAdapterIndex=trnCpqAdapterIndex, trnCpqInitDMATimeoutErrors=trnCpqInitDMATimeoutErrors, trnCpqAdapterCheckStatsIndex=trnCpqAdapterCheckStatsIndex, trnCpqBUDStatsTable=trnCpqBUDStatsTable, trnCpqSystemInterfaceRegErrors=trnCpqSystemInterfaceRegErrors, trnCpqBUDStatsEntry=trnCpqBUDStatsEntry, trnCpqRingSpeedDetect=trnCpqRingSpeedDetect, trnCpqRegParityErrors=trnCpqRegParityErrors)
