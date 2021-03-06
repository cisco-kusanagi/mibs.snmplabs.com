#
# PySNMP MIB module A3COM-HUAWEI-TRANSCEIVER-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-TRANSCEIVER-INFO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:07:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ifIndex, ifEntry = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifEntry")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Integer32, Counter64, Unsigned32, IpAddress, MibIdentifier, ModuleIdentity, Counter32, ObjectIdentity, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Integer32", "Counter64", "Unsigned32", "IpAddress", "MibIdentifier", "ModuleIdentity", "Counter32", "ObjectIdentity", "Gauge32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
h3cTransceiver = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 70))
h3cTransceiver.setRevisions(('2009-12-29 16:50',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cTransceiver.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: h3cTransceiver.setLastUpdated('200912291650Z')
if mibBuilder.loadTexts: h3cTransceiver.setOrganization('H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cTransceiver.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: h3cTransceiver.setDescription('The objects in this MIB module are used to display the information of transceiver on interface.')
h3cTransceiverInfoAdm = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 70, 1))
h3cTransceiverInfoTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 70, 1, 1), )
if mibBuilder.loadTexts: h3cTransceiverInfoTable.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverInfoTable.setDescription('This table show the information of transceiver on interface.')
h3cTransceiverInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 70, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cTransceiverInfoEntry.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverInfoEntry.setDescription('The entry of the h3cTransceiverInfoTable.')
h3cTransceiverHardwareType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 70, 1, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverHardwareType.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverHardwareType.setDescription('Hardware type of the interface, such as SM(single mode).')
h3cTransceiverType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 70, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverType.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverType.setDescription('Type of the interface, such as SFP/XFP/GBIC.')
h3cTransceiverWaveLength = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 70, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverWaveLength.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverWaveLength.setDescription('Wave length of the interface, measured in nanometer.')
h3cTransceiverVendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 70, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverVendorName.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverVendorName.setDescription('Vendor name of the interface.')
h3cTransceiverSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 70, 1, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverSerialNumber.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverSerialNumber.setDescription('Serial number of the interface.')
h3cTransceiverFiberDiameterType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 70, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 65535))).clone(namedValues=NamedValues(("fiber9", 1), ("fiber50", 2), ("fiber625", 3), ("copper", 4), ("unknown", 65535)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverFiberDiameterType.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverFiberDiameterType.setDescription('The diameter of the fiber, measured in micron. fiber9 - 9 micron multi-mode fiber fiber50 - 50 micron multi-mode fiber fiber625 - 62.5 micron multi-mode fiber copper - copper cable.')
h3cTransceiverTransferDistance = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 70, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverTransferDistance.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverTransferDistance.setDescription('The maximal distance which the interface could transmit, measured in meter.')
h3cTransceiverDiagnostic = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 70, 1, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverDiagnostic.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverDiagnostic.setDescription('Indicating the digital diagnostic monitoring function .')
h3cTransceiverCurTXPower = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 70, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverCurTXPower.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverCurTXPower.setDescription('Indicating the current transmitted power . The unit is in hundredths of dBM.')
h3cTransceiverMaxTXPower = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 70, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverMaxTXPower.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverMaxTXPower.setDescription('Indicating the maximal transmitted power . The unit is in hundredths of dBM.')
h3cTransceiverMinTXPower = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 70, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverMinTXPower.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverMinTXPower.setDescription('Indicating the minimal transmitted power . The unit is in hundredths of dBM.')
h3cTransceiverCurRXPower = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 70, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverCurRXPower.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverCurRXPower.setDescription('Indicating the current received power . The unit is in hundredths of dBM.')
h3cTransceiverMaxRXPower = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 70, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverMaxRXPower.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverMaxRXPower.setDescription('Indicating the maximal received power . The unit is in hundredths of dBM.')
h3cTransceiverMinRXPower = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 70, 1, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverMinRXPower.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverMinRXPower.setDescription('Indicating the minimal received power . The unit is in hundredths of dBM.')
h3cTransceiverTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 70, 1, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverTemperature.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverTemperature.setDescription('Indicating the current temperature. The unit is celsius. ')
h3cTransceiverVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 70, 1, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverVoltage.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverVoltage.setDescription('Indicating the current voltage . The unit is in hundredths of V')
h3cTransceiverBiasCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 70, 1, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverBiasCurrent.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverBiasCurrent.setDescription('Indicating the current bias electric current . The unit is in hundredths of mA')
mibBuilder.exportSymbols("A3COM-HUAWEI-TRANSCEIVER-INFO-MIB", h3cTransceiverMaxRXPower=h3cTransceiverMaxRXPower, h3cTransceiverCurRXPower=h3cTransceiverCurRXPower, h3cTransceiverInfoTable=h3cTransceiverInfoTable, h3cTransceiverVoltage=h3cTransceiverVoltage, PYSNMP_MODULE_ID=h3cTransceiver, h3cTransceiverDiagnostic=h3cTransceiverDiagnostic, h3cTransceiverTransferDistance=h3cTransceiverTransferDistance, h3cTransceiver=h3cTransceiver, h3cTransceiverMinRXPower=h3cTransceiverMinRXPower, h3cTransceiverSerialNumber=h3cTransceiverSerialNumber, h3cTransceiverHardwareType=h3cTransceiverHardwareType, h3cTransceiverType=h3cTransceiverType, h3cTransceiverInfoAdm=h3cTransceiverInfoAdm, h3cTransceiverCurTXPower=h3cTransceiverCurTXPower, h3cTransceiverTemperature=h3cTransceiverTemperature, h3cTransceiverBiasCurrent=h3cTransceiverBiasCurrent, h3cTransceiverInfoEntry=h3cTransceiverInfoEntry, h3cTransceiverWaveLength=h3cTransceiverWaveLength, h3cTransceiverFiberDiameterType=h3cTransceiverFiberDiameterType, h3cTransceiverMinTXPower=h3cTransceiverMinTXPower, h3cTransceiverMaxTXPower=h3cTransceiverMaxTXPower, h3cTransceiverVendorName=h3cTransceiverVendorName)
