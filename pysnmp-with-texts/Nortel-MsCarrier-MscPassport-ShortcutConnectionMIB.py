#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-ShortcutConnectionMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-ShortcutConnectionMIB
# Produced by pysmi-0.3.4 at Wed May  1 14:31:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
StorageType, RowPointer, Unsigned32, Integer32, RowStatus, Counter32, DisplayString = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "StorageType", "RowPointer", "Unsigned32", "Integer32", "RowStatus", "Counter32", "DisplayString")
NonReplicated, HexString = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", "NonReplicated", "HexString")
mscPassportMIBs, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs")
mscVrPpIndex, mscVrIndex, mscVrPp = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex", "mscVrIndex", "mscVrPp")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ObjectIdentity, iso, IpAddress, MibIdentifier, TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, Unsigned32, Counter64, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "iso", "IpAddress", "MibIdentifier", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "Unsigned32", "Counter64", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
shortcutConnectionMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 78))
mscVrPpSc = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16))
mscVrPpScRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 1), )
if mibBuilder.loadTexts: mscVrPpScRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScRowStatusTable.setDescription('*** THIS TABLE CURRENTLY NOT IMPLEMENTED *** This entry controls the addition and deletion of mscVrPpSc components.')
mscVrPpScRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"), (0, "Nortel-MsCarrier-MscPassport-ShortcutConnectionMIB", "mscVrPpScIndex"))
if mibBuilder.loadTexts: mscVrPpScRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScRowStatusEntry.setDescription('A single entry in the table represents a single mscVrPpSc component.')
mscVrPpScRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrPpScRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScRowStatus.setDescription('This variable is used as the basis for SNMP naming of mscVrPpSc components. These components cannot be added nor deleted.')
mscVrPpScComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrPpScComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
mscVrPpScStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrPpScStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScStorageType.setDescription('This variable represents the storage type value for the mscVrPpSc tables.')
mscVrPpScIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023)))
if mibBuilder.loadTexts: mscVrPpScIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScIndex.setDescription('This variable represents the index for the mscVrPpSc tables.')
mscVrPpScOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 10), )
if mibBuilder.loadTexts: mscVrPpScOperTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScOperTable.setDescription('*** THIS TABLE CURRENTLY NOT IMPLEMENTED *** This group contains the operational status attributes of the ShortcutConnection component.')
mscVrPpScOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"), (0, "Nortel-MsCarrier-MscPassport-ShortcutConnectionMIB", "mscVrPpScIndex"))
if mibBuilder.loadTexts: mscVrPpScOperEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScOperEntry.setDescription('An entry in the mscVrPpScOperTable.')
mscVrPpScRemoteNbmaAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 10, 1, 1), HexString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrPpScRemoteNbmaAddress.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScRemoteNbmaAddress.setDescription('This attribute indicates the NBMA address of the far (remote) end.')
mscVrPpScAge = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4292967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrPpScAge.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScAge.setDescription('This attribute indicates how long the connection has been up.')
mscVrPpScMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 10, 1, 3), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(576, 18944), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrPpScMtu.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScMtu.setDescription('This attribute indicates the Layer 2 MTU (that is, CPCS-SDU for ATM) of this connection.')
mscVrPpScConnSource = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 10, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrPpScConnSource.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScConnSource.setDescription('This attributes indicates which end originated the connect request for this connection.')
mscVrPpScType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 10, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unidirectional", 1), ("bidirectional", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrPpScType.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScType.setDescription('This attributes indicates the type of this connection.')
mscVrPpScStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 11), )
if mibBuilder.loadTexts: mscVrPpScStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScStatsTable.setDescription('*** THIS TABLE CURRENTLY NOT IMPLEMENTED *** This group contains the statistical attributes of the ShortcutConnection component.')
mscVrPpScStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"), (0, "Nortel-MsCarrier-MscPassport-ShortcutConnectionMIB", "mscVrPpScIndex"))
if mibBuilder.loadTexts: mscVrPpScStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScStatsEntry.setDescription('An entry in the mscVrPpScStatsTable.')
mscVrPpScTxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 11, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrPpScTxFrames.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScTxFrames.setDescription('This attribute counts the frames transmitted over this connection. This counter wraps to zero when the maximum value is exceeded.')
mscVrPpScRxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 11, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrPpScRxFrames.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScRxFrames.setDescription('This attributes counts the frames received over this connection. This counter wraps to zero when the maximum value is exceeded.')
mscVrPpScAtmCon = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 4))
mscVrPpScAtmConRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 4, 1), )
if mibBuilder.loadTexts: mscVrPpScAtmConRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScAtmConRowStatusTable.setDescription('*** THIS TABLE CURRENTLY NOT IMPLEMENTED *** This entry controls the addition and deletion of mscVrPpScAtmCon components.')
mscVrPpScAtmConRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 4, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"), (0, "Nortel-MsCarrier-MscPassport-ShortcutConnectionMIB", "mscVrPpScIndex"), (0, "Nortel-MsCarrier-MscPassport-ShortcutConnectionMIB", "mscVrPpScAtmConIndex"))
if mibBuilder.loadTexts: mscVrPpScAtmConRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScAtmConRowStatusEntry.setDescription('A single entry in the table represents a single mscVrPpScAtmCon component.')
mscVrPpScAtmConRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 4, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrPpScAtmConRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScAtmConRowStatus.setDescription('This variable is used as the basis for SNMP naming of mscVrPpScAtmCon components. These components cannot be added nor deleted.')
mscVrPpScAtmConComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 4, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrPpScAtmConComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScAtmConComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
mscVrPpScAtmConStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 4, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrPpScAtmConStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScAtmConStorageType.setDescription('This variable represents the storage type value for the mscVrPpScAtmCon tables.')
mscVrPpScAtmConIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 4, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscVrPpScAtmConIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScAtmConIndex.setDescription('This variable represents the index for the mscVrPpScAtmCon tables.')
mscVrPpScAtmConOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 4, 10), )
if mibBuilder.loadTexts: mscVrPpScAtmConOperTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScAtmConOperTable.setDescription('*** THIS TABLE CURRENTLY NOT IMPLEMENTED *** This attribute group contains the operational attributes for the NapAtmConnection component.')
mscVrPpScAtmConOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 4, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"), (0, "Nortel-MsCarrier-MscPassport-ShortcutConnectionMIB", "mscVrPpScIndex"), (0, "Nortel-MsCarrier-MscPassport-ShortcutConnectionMIB", "mscVrPpScAtmConIndex"))
if mibBuilder.loadTexts: mscVrPpScAtmConOperEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScAtmConOperEntry.setDescription('An entry in the mscVrPpScAtmConOperTable.')
mscVrPpScAtmConNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 4, 10, 1, 1), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrPpScAtmConNextHop.setStatus('mandatory')
if mibBuilder.loadTexts: mscVrPpScAtmConNextHop.setDescription('This attribute shows the component name of the AtmIf Vcc Ep or AtmCon component to which this switched connection is established.')
shortcutConnectionGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 78, 1))
shortcutConnectionGroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 78, 1, 1))
shortcutConnectionGroupCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 78, 1, 1, 3))
shortcutConnectionGroupCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 78, 1, 1, 3, 2))
shortcutConnectionCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 78, 3))
shortcutConnectionCapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 78, 3, 1))
shortcutConnectionCapabilitiesCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 78, 3, 1, 3))
shortcutConnectionCapabilitiesCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 78, 3, 1, 3, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-ShortcutConnectionMIB", mscVrPpScAtmConOperEntry=mscVrPpScAtmConOperEntry, mscVrPpScAge=mscVrPpScAge, mscVrPpScAtmConRowStatus=mscVrPpScAtmConRowStatus, shortcutConnectionGroupCA02=shortcutConnectionGroupCA02, shortcutConnectionCapabilities=shortcutConnectionCapabilities, mscVrPpScAtmConIndex=mscVrPpScAtmConIndex, mscVrPpScOperTable=mscVrPpScOperTable, mscVrPpScAtmConOperTable=mscVrPpScAtmConOperTable, shortcutConnectionCapabilitiesCA=shortcutConnectionCapabilitiesCA, mscVrPpScType=mscVrPpScType, mscVrPpScMtu=mscVrPpScMtu, mscVrPpScStatsEntry=mscVrPpScStatsEntry, shortcutConnectionGroupCA=shortcutConnectionGroupCA, mscVrPpScRowStatusTable=mscVrPpScRowStatusTable, mscVrPpScAtmConNextHop=mscVrPpScAtmConNextHop, mscVrPpScRxFrames=mscVrPpScRxFrames, mscVrPpScAtmConStorageType=mscVrPpScAtmConStorageType, mscVrPpSc=mscVrPpSc, shortcutConnectionGroup=shortcutConnectionGroup, mscVrPpScStorageType=mscVrPpScStorageType, mscVrPpScAtmConRowStatusTable=mscVrPpScAtmConRowStatusTable, mscVrPpScTxFrames=mscVrPpScTxFrames, shortcutConnectionCapabilitiesCA02A=shortcutConnectionCapabilitiesCA02A, mscVrPpScRowStatusEntry=mscVrPpScRowStatusEntry, mscVrPpScOperEntry=mscVrPpScOperEntry, mscVrPpScAtmConRowStatusEntry=mscVrPpScAtmConRowStatusEntry, shortcutConnectionGroupCA02A=shortcutConnectionGroupCA02A, mscVrPpScStatsTable=mscVrPpScStatsTable, shortcutConnectionCapabilitiesCA02=shortcutConnectionCapabilitiesCA02, mscVrPpScIndex=mscVrPpScIndex, mscVrPpScConnSource=mscVrPpScConnSource, mscVrPpScRemoteNbmaAddress=mscVrPpScRemoteNbmaAddress, shortcutConnectionMIB=shortcutConnectionMIB, mscVrPpScAtmCon=mscVrPpScAtmCon, mscVrPpScAtmConComponentName=mscVrPpScAtmConComponentName, mscVrPpScComponentName=mscVrPpScComponentName, mscVrPpScRowStatus=mscVrPpScRowStatus)