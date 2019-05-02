#
# PySNMP MIB module EATON-PDU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EATON-PDU-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:59:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
pduAgent, = mibBuilder.importSymbols("EATON-OIDS", "pduAgent")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, IpAddress, Gauge32, Integer32, ModuleIdentity, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, NotificationType, Counter32, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "Gauge32", "Integer32", "ModuleIdentity", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "NotificationType", "Counter32", "ObjectIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eatonPduMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 534, 6, 6, 4))
eatonPduMIB.setRevisions(('2007-01-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eatonPduMIB.setRevisionsDescriptions(('Initial Version of eatonPduMIB. Provides objects for PDU, Panel, and Breaker levels.',))
if mibBuilder.loadTexts: eatonPduMIB.setLastUpdated('200701080000Z')
if mibBuilder.loadTexts: eatonPduMIB.setOrganization('Eaton Corporation')
if mibBuilder.loadTexts: eatonPduMIB.setContactInfo('Eaton Power Quality Technical Support (PQTS) group www.eaton.com/powerxpert Technical Resource Center phone numbers United States: 1.800.843.9433 or 919.870.3028 Canada: 1.800.461.9166 ext. 260 All other countries: Call your local service representative.')
if mibBuilder.loadTexts: eatonPduMIB.setDescription('The MIB module for Eaton PDUs (Power Distribution Units). Copyright (C) Eaton Corporation (2007).')
class PositiveInteger(TextualConvention, Integer32):
    description = 'This data type is a non-zero and non-negative value.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class NonNegativeInteger(TextualConvention, Integer32):
    description = 'This data type is a non-negative value.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

eatonPduMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1))
mainPdu = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1))
pduPanel = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2))
pduBreaker = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3))
pduNameplate = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 1))
pduRatingVA = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 1, 1), PositiveInteger()).setUnits('volt-amps').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduRatingVA.setStatus('current')
if mibBuilder.loadTexts: pduRatingVA.setDescription('The full VA rating of this PDU (for all phases).')
pduNominalOutputVoltage = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 1, 2), PositiveInteger()).setUnits('Volts RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduNominalOutputVoltage.setStatus('current')
if mibBuilder.loadTexts: pduNominalOutputVoltage.setDescription('The nominal Output Voltage of this PDU (as distributed to the panels). May differ from the nominal Input Voltage if the PDU has an input transformer. This is either Line-to-Line or Line-to-Neutral, as indicated in pduOutputVoltageUnits.')
pduNumPhases = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 1, 3), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pduNumPhases.setStatus('current')
if mibBuilder.loadTexts: pduNumPhases.setDescription('The number of lines (phases) for this PDU. The number of Input phases must equal the number of Output phases.')
pduNumPanels = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 1, 4), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pduNumPanels.setStatus('current')
if mibBuilder.loadTexts: pduNumPanels.setDescription('The number of panels or subfeeds contained in this PDU system. This determines the number of rows found in the panel tables.')
pduInput = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2))
pduFrequency = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 1), NonNegativeInteger()).setUnits('0.1 Hertz').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduFrequency.setStatus('current')
if mibBuilder.loadTexts: pduFrequency.setDescription('The present frequency reading for the full PDU.')
pduInputVA = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 2), NonNegativeInteger()).setUnits('VA').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduInputVA.setStatus('current')
if mibBuilder.loadTexts: pduInputVA.setDescription('The present VA input demand of the full PDU system.')
pduInputPower = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 3), NonNegativeInteger()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduInputPower.setStatus('current')
if mibBuilder.loadTexts: pduInputPower.setDescription('The present input power demand of the full PDU system.')
pduInputPowerFactor = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 100))).setUnits('pf * 100').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduInputPowerFactor.setStatus('current')
if mibBuilder.loadTexts: pduInputPowerFactor.setDescription('The input power factor for the full PDU system. Varies from -1.00 to 1.00, multiplied by 100. If negative values are used, they indicate lagging pf.')
pduGroundCurrent = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 5), NonNegativeInteger()).setUnits('0.1 Amps RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduGroundCurrent.setStatus('current')
if mibBuilder.loadTexts: pduGroundCurrent.setDescription("The present current in the PDU's ground phase. Ideally, this value stays at 0.")
pduInputVoltageUnits = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pduInputVoltageUnits.setStatus('current')
if mibBuilder.loadTexts: pduInputVoltageUnits.setDescription("Indicates whether the pduInputPhaseVoltage readings are 'Vrms Line-Line' or 'Vrms Line-Neutral'.")
pduInputNumPhases = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 7), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pduInputNumPhases.setStatus('current')
if mibBuilder.loadTexts: pduInputNumPhases.setDescription('The number of input phases for this PDU. This variable indicates the number of rows in the pduInputTable.')
pduInputTable = MibTable((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 8), )
if mibBuilder.loadTexts: pduInputTable.setStatus('current')
if mibBuilder.loadTexts: pduInputTable.setDescription('A list of input table entries. The number of entries is given by the value of pduInputNumPhases.')
pduInputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 8, 1), ).setIndexNames((0, "EATON-PDU-MIB", "pduInputPhaseIndex"))
if mibBuilder.loadTexts: pduInputEntry.setStatus('current')
if mibBuilder.loadTexts: pduInputEntry.setDescription('An entry containing information applicable to a particular input phase.')
pduInputPhaseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 8, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: pduInputPhaseIndex.setStatus('current')
if mibBuilder.loadTexts: pduInputPhaseIndex.setDescription('The input line identifier.')
pduInputPhaseVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 8, 1, 2), NonNegativeInteger()).setUnits('Volts RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduInputPhaseVoltage.setStatus('current')
if mibBuilder.loadTexts: pduInputPhaseVoltage.setDescription('The present input voltage for this phase.')
pduInputPhaseCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 8, 1, 3), NonNegativeInteger()).setUnits('0.1 Amps RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduInputPhaseCurrent.setStatus('current')
if mibBuilder.loadTexts: pduInputPhaseCurrent.setDescription('The present input current for this phase.')
pduInputPhasePercentLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 8, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduInputPhasePercentLoad.setStatus('current')
if mibBuilder.loadTexts: pduInputPhasePercentLoad.setDescription('The percentage of the pdu power capacity presently being used on this line, normally based on the ratio of pduInputPhaseCurrent to the rated input current.')
pduOutput = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3))
pduOutputKilowattHours = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 1), NonNegativeInteger()).setUnits('KWH').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduOutputKilowattHours.setStatus('current')
if mibBuilder.loadTexts: pduOutputKilowattHours.setDescription('The accumulated kilowatt-hour value for the full PDU system since the last reset.')
pduOutputVA = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 2), NonNegativeInteger()).setUnits('VA').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduOutputVA.setStatus('current')
if mibBuilder.loadTexts: pduOutputVA.setDescription('The present VA output of the full PDU system.')
pduOutputPower = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 3), NonNegativeInteger()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduOutputPower.setStatus('current')
if mibBuilder.loadTexts: pduOutputPower.setDescription('The present output power of the full PDU system.')
pduOutputPowerFactor = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 100))).setUnits('pf * 100').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduOutputPowerFactor.setStatus('current')
if mibBuilder.loadTexts: pduOutputPowerFactor.setDescription('The output power factor for the full PDU system. Varies from -1.00 to 1.00, multiplied by 100. If negative values are used, they indicate lagging pf.')
pduNeutralCurrent = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 5), NonNegativeInteger()).setUnits('0.1 Amps RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduNeutralCurrent.setStatus('current')
if mibBuilder.loadTexts: pduNeutralCurrent.setDescription("The present current in the PDU's output neutral phase. Ideally, this value stays at 0.")
pduRatedOutputCurrent = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 6), PositiveInteger()).setUnits('0.1 Amps RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduRatedOutputCurrent.setStatus('current')
if mibBuilder.loadTexts: pduRatedOutputCurrent.setDescription('The rated current value for one PDU Output phase at full load (100%).')
pduOutputVoltageUnits = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pduOutputVoltageUnits.setStatus('current')
if mibBuilder.loadTexts: pduOutputVoltageUnits.setDescription("Indicates whether the pduOutputPhaseVoltage readings are 'Vrms Line-Line' or 'Vrms Line-Neutral'.")
pduOutputNumPhases = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 8), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pduOutputNumPhases.setStatus('current')
if mibBuilder.loadTexts: pduOutputNumPhases.setDescription('The number of output phases for this PDU. This variable indicates the number of rows in the pduOutputTable.')
pduOutputTable = MibTable((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 9), )
if mibBuilder.loadTexts: pduOutputTable.setStatus('current')
if mibBuilder.loadTexts: pduOutputTable.setDescription('A list of output table entries. The number of entries is given by the value of pduOutputNumPhases.')
pduOutputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 9, 1), ).setIndexNames((0, "EATON-PDU-MIB", "pduOutputPhaseIndex"))
if mibBuilder.loadTexts: pduOutputEntry.setStatus('current')
if mibBuilder.loadTexts: pduOutputEntry.setDescription('An entry containing information applicable to a particular output phase.')
pduOutputPhaseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 9, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: pduOutputPhaseIndex.setStatus('current')
if mibBuilder.loadTexts: pduOutputPhaseIndex.setDescription('The output line identifier.')
pduOutputPhaseVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 9, 1, 2), NonNegativeInteger()).setUnits('Volts RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduOutputPhaseVoltage.setStatus('current')
if mibBuilder.loadTexts: pduOutputPhaseVoltage.setDescription('The present output voltage for this phase.')
pduOutputPhaseCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 9, 1, 3), NonNegativeInteger()).setUnits('0.1 Amps RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduOutputPhaseCurrent.setStatus('current')
if mibBuilder.loadTexts: pduOutputPhaseCurrent.setDescription('The present output current for this phase.')
pduOutputPhasePercentLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 9, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduOutputPhasePercentLoad.setStatus('current')
if mibBuilder.loadTexts: pduOutputPhasePercentLoad.setDescription('The percentage of the pdu power capacity presently being used on this line, normally based on the ratio of pduOutputPhaseCurrent to pduRatedOutputCurrent.')
panelRatingsTable = MibTable((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1), )
if mibBuilder.loadTexts: panelRatingsTable.setStatus('current')
if mibBuilder.loadTexts: panelRatingsTable.setDescription('A sparsely populated (ie, not sequentially numbered) table of ratings for each panel. The number of entries is given by the value of pduNumPanels.')
panelRatingsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1, 1), ).setIndexNames((0, "EATON-PDU-MIB", "panelNumber"))
if mibBuilder.loadTexts: panelRatingsEntry.setStatus('current')
if mibBuilder.loadTexts: panelRatingsEntry.setDescription('An entry containing information applicable to a particular output phase.')
panelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: panelNumber.setStatus('current')
if mibBuilder.loadTexts: panelNumber.setDescription('Index for the Panel Ratings and Meters tables. Corresponds to the physical panel number in the PDU system. There must be a #1. The maximum value is 16. Panels are not required to be numbered sequentially.')
panelRatedVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1, 1, 2), PositiveInteger()).setUnits('Volts RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelRatedVoltage.setStatus('current')
if mibBuilder.loadTexts: panelRatedVoltage.setDescription('The nominal Voltage of this panel (as distributed to the breakers or subfeeds). This is either Line-to-Line or Line-to-Neutral, as indicated in panelVoltageUnits.')
panelRatedBreakerCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1, 1, 3), PositiveInteger()).setUnits('0.1 Amps RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelRatedBreakerCurrent.setStatus('current')
if mibBuilder.loadTexts: panelRatedBreakerCurrent.setDescription("The rated current value for one panel (input) phase at full load (100%). This is set by the panel's input breaker; if there is no input breaker for this panel, then this object is not accessible.")
panelNumPhases = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1, 1, 4), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panelNumPhases.setStatus('current')
if mibBuilder.loadTexts: panelNumPhases.setDescription('The number of lines (phases) for this panel.')
panelNumBreakers = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1, 1, 5), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panelNumBreakers.setStatus('current')
if mibBuilder.loadTexts: panelNumBreakers.setDescription('The number of breakers contained in this panel. This determines the number of rows found in the breaker tables.')
panelVoltageUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: panelVoltageUnits.setStatus('current')
if mibBuilder.loadTexts: panelVoltageUnits.setDescription("Indicates whether the panelPhaseVoltage readings are 'Vrms Line-Line' or 'Vrms Line-Neutral'.")
panelMetersTable = MibTable((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2), )
if mibBuilder.loadTexts: panelMetersTable.setStatus('current')
if mibBuilder.loadTexts: panelMetersTable.setDescription('A sparsely populated (ie, not sequentially numbered) table of ratings for each panel. The number of entries is given by the value of pduNumPanels.')
panelMetersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1), ).setIndexNames((0, "EATON-PDU-MIB", "panelNumber"))
if mibBuilder.loadTexts: panelMetersEntry.setStatus('current')
if mibBuilder.loadTexts: panelMetersEntry.setDescription('An entry containing meter readings applicable to a particular panel.')
panelTotalKilowattHours = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1, 1), NonNegativeInteger()).setUnits('KWH').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelTotalKilowattHours.setStatus('current')
if mibBuilder.loadTexts: panelTotalKilowattHours.setDescription('The accumulated kilowatt-hours for this panel since it was commissioned and put into service, or since the last reset of the system KHW measures.')
panelMonthlyKilowattHours = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1, 2), NonNegativeInteger()).setUnits('KWH').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelMonthlyKilowattHours.setStatus('current')
if mibBuilder.loadTexts: panelMonthlyKilowattHours.setDescription('The accumulated kilowatt-hours for this panel since the beginning of this calendar month, or since the last reset of the system KHW measures.')
panelYtdKilowattHours = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1, 3), NonNegativeInteger()).setUnits('KWH').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelYtdKilowattHours.setStatus('current')
if mibBuilder.loadTexts: panelYtdKilowattHours.setDescription('The accumulated kilowatt-hours for this panel since the beginning of this calendar year (YTD), or since the last reset of the system KHW measures.')
panelVA = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1, 4), NonNegativeInteger()).setUnits('VA').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelVA.setStatus('current')
if mibBuilder.loadTexts: panelVA.setDescription('The present VA (input) demand of this panel.')
panelPower = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1, 5), NonNegativeInteger()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelPower.setStatus('current')
if mibBuilder.loadTexts: panelPower.setDescription('The present power (input) demand of this panel.')
panelPowerFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 100))).setUnits('pf * 100').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelPowerFactor.setStatus('current')
if mibBuilder.loadTexts: panelPowerFactor.setDescription('The input power factor for this panel. Varies from -1.00 to 1.00, multiplied by 100. If negative values are used, they indicate lagging pf.')
panelNeutralCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1, 7), NonNegativeInteger()).setUnits('0.1 Amps RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelNeutralCurrent.setStatus('current')
if mibBuilder.loadTexts: panelNeutralCurrent.setDescription('The present neutral phase current for this panel.')
panelPhaseMetersTable = MibTable((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 3), )
if mibBuilder.loadTexts: panelPhaseMetersTable.setStatus('current')
if mibBuilder.loadTexts: panelPhaseMetersTable.setDescription('A sparsely populated (ie, not sequentially panel numbered) table of ratings for each panel. The number of entries is given by the sum of panelNumPhases for pduNumPanels.')
panelPhaseMetersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 3, 1), ).setIndexNames((0, "EATON-PDU-MIB", "panelNumber"), (0, "EATON-PDU-MIB", "panelPhaseIndex"))
if mibBuilder.loadTexts: panelPhaseMetersEntry.setStatus('current')
if mibBuilder.loadTexts: panelPhaseMetersEntry.setDescription('An entry containing meter readings applicable to a particular phase of a particular panel.')
panelPhaseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 3, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: panelPhaseIndex.setStatus('current')
if mibBuilder.loadTexts: panelPhaseIndex.setDescription('The line or phase identifier.')
panelPhaseVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 3, 1, 2), NonNegativeInteger()).setUnits('Volts RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelPhaseVoltage.setStatus('current')
if mibBuilder.loadTexts: panelPhaseVoltage.setDescription('The present voltage for this phase.')
panelPhaseCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 3, 1, 3), NonNegativeInteger()).setUnits('0.1 Amps RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelPhaseCurrent.setStatus('current')
if mibBuilder.loadTexts: panelPhaseCurrent.setDescription('The present current for this phase.')
panelPhasePercentLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelPhasePercentLoad.setStatus('current')
if mibBuilder.loadTexts: panelPhasePercentLoad.setDescription('The percentage of the panel power capacity presently being used on this line, normally based on the ratio of panelPhaseCurrent to the rated phase current.')
breakerRatingsTable = MibTable((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 1), )
if mibBuilder.loadTexts: breakerRatingsTable.setStatus('current')
if mibBuilder.loadTexts: breakerRatingsTable.setDescription('A sparsely populated (ie, not sequentially numbered) table of ratings and fixed values for each breaker. The number of entries is given by the value of panelNumBreakers for this panel.')
breakerRatingsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 1, 1), ).setIndexNames((0, "EATON-PDU-MIB", "panelNumber"), (0, "EATON-PDU-MIB", "breakerNumber"))
if mibBuilder.loadTexts: breakerRatingsEntry.setStatus('current')
if mibBuilder.loadTexts: breakerRatingsEntry.setDescription('An entry containing information applicable to a particular output phase.')
breakerNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 1, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: breakerNumber.setStatus('current')
if mibBuilder.loadTexts: breakerNumber.setDescription('Index for the Breaker Ratings and Meters tables. Corresponds to the physical breaker number in the PDU system. Breakers are not required to be numbered sequentially.')
breakerName = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: breakerName.setStatus('current')
if mibBuilder.loadTexts: breakerName.setDescription('Name given by the administrator to identify this breaker.')
breakerRatedCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 1, 1, 3), PositiveInteger()).setUnits('0.1 Amps RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: breakerRatedCurrent.setStatus('current')
if mibBuilder.loadTexts: breakerRatedCurrent.setDescription('The rated current value of this breaker (for one phase) at full load (100%).')
breakerNumPhases = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 1, 1, 4), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: breakerNumPhases.setStatus('current')
if mibBuilder.loadTexts: breakerNumPhases.setDescription('The number of lines (phases) for this breaker.')
breakerMetersTable = MibTable((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 2), )
if mibBuilder.loadTexts: breakerMetersTable.setStatus('current')
if mibBuilder.loadTexts: breakerMetersTable.setDescription('A sparsely populated (ie, not sequentially numbered) table of ratings for each breaker. The number of entries is given by the value of panelNumBreakers for this panel.')
breakerMetersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 2, 1), ).setIndexNames((0, "EATON-PDU-MIB", "panelNumber"), (0, "EATON-PDU-MIB", "breakerNumber"))
if mibBuilder.loadTexts: breakerMetersEntry.setStatus('current')
if mibBuilder.loadTexts: breakerMetersEntry.setDescription('An entry containing meter readings applicable to a particular breaker.')
breakerTotalKilowattHours = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 2, 1, 1), NonNegativeInteger()).setUnits('KWH').setMaxAccess("readonly")
if mibBuilder.loadTexts: breakerTotalKilowattHours.setStatus('current')
if mibBuilder.loadTexts: breakerTotalKilowattHours.setDescription('The accumulated kilowatt-hours for this breaker since it was commissioned and put into service, or since the last reset of the panel KHW measures.')
breakerMonthlyKilowattHours = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 2, 1, 2), NonNegativeInteger()).setUnits('KWH').setMaxAccess("readonly")
if mibBuilder.loadTexts: breakerMonthlyKilowattHours.setStatus('current')
if mibBuilder.loadTexts: breakerMonthlyKilowattHours.setDescription('The accumulated kilowatt-hours for this breaker since the beginning of this calendar month, or since the last reset of the panel KHW measures.')
breakerYtdKilowattHours = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 2, 1, 3), NonNegativeInteger()).setUnits('KWH').setMaxAccess("readonly")
if mibBuilder.loadTexts: breakerYtdKilowattHours.setStatus('current')
if mibBuilder.loadTexts: breakerYtdKilowattHours.setDescription('The accumulated kilowatt-hours for this breaker since the beginning of this calendar year (YTD), or since the last reset of the panel KHW measures.')
breakerPhaseMetersTable = MibTable((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3), )
if mibBuilder.loadTexts: breakerPhaseMetersTable.setStatus('current')
if mibBuilder.loadTexts: breakerPhaseMetersTable.setDescription('A sparsely populated (ie, not sequentially breaker numbered) table of ratings for each breaker. The number of entries is given by the sum of breakerNumPhases for panelNumBreakers for all panels (pduNumPanels).')
breakerPhaseMetersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3, 1), ).setIndexNames((0, "EATON-PDU-MIB", "panelNumber"), (0, "EATON-PDU-MIB", "breakerNumber"), (0, "EATON-PDU-MIB", "breakerPhaseIndex"))
if mibBuilder.loadTexts: breakerPhaseMetersEntry.setStatus('current')
if mibBuilder.loadTexts: breakerPhaseMetersEntry.setDescription('An entry containing meter readings applicable to a particular phase of a particular breaker on a particular panel.')
breakerPhaseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: breakerPhaseIndex.setStatus('current')
if mibBuilder.loadTexts: breakerPhaseIndex.setDescription('The line or phase identifier.')
breakerPhaseVA = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3, 1, 2), NonNegativeInteger()).setUnits('VA').setMaxAccess("readonly")
if mibBuilder.loadTexts: breakerPhaseVA.setStatus('current')
if mibBuilder.loadTexts: breakerPhaseVA.setDescription('The present VA (input) demand of this phase on this breaker.')
breakerPhasePower = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3, 1, 3), NonNegativeInteger()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: breakerPhasePower.setStatus('current')
if mibBuilder.loadTexts: breakerPhasePower.setDescription('The present power (input) demand of phase on this breaker.')
breakerPhasePowerFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 100))).setUnits('pf * 100').setMaxAccess("readonly")
if mibBuilder.loadTexts: breakerPhasePowerFactor.setStatus('current')
if mibBuilder.loadTexts: breakerPhasePowerFactor.setDescription('The input power factor for this phase on this breaker. Varies from -1.00 to 1.00, multiplied by 100. If negative values are used, they indicate lagging pf.')
breakerPhaseCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3, 1, 5), NonNegativeInteger()).setUnits('0.1 Amps RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: breakerPhaseCurrent.setStatus('current')
if mibBuilder.loadTexts: breakerPhaseCurrent.setDescription('The present current for this phase of this breaker.')
breakerPhasePercentLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: breakerPhasePercentLoad.setStatus('current')
if mibBuilder.loadTexts: breakerPhasePercentLoad.setDescription('The percentage of the breaker power capacity presently being used on this line, normally based on the ratio of breakerPhaseCurrent to the breakerRatedCurrent.')
eatonPduConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2))
pduNameplateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 1)).setObjects(("EATON-PDU-MIB", "pduNumPhases"), ("EATON-PDU-MIB", "pduNominalOutputVoltage"), ("EATON-PDU-MIB", "pduRatingVA"), ("EATON-PDU-MIB", "pduNumPanels"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pduNameplateGroup = pduNameplateGroup.setStatus('current')
if mibBuilder.loadTexts: pduNameplateGroup.setDescription('The pduNameplate subgroup objects.')
pduInputGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 2)).setObjects(("EATON-PDU-MIB", "pduFrequency"), ("EATON-PDU-MIB", "pduInputVA"), ("EATON-PDU-MIB", "pduInputPower"), ("EATON-PDU-MIB", "pduInputPowerFactor"), ("EATON-PDU-MIB", "pduGroundCurrent"), ("EATON-PDU-MIB", "pduInputVoltageUnits"), ("EATON-PDU-MIB", "pduInputNumPhases"), ("EATON-PDU-MIB", "pduInputPhaseVoltage"), ("EATON-PDU-MIB", "pduInputPhaseCurrent"), ("EATON-PDU-MIB", "pduInputPhasePercentLoad"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pduInputGroup = pduInputGroup.setStatus('current')
if mibBuilder.loadTexts: pduInputGroup.setDescription('The pduInput Meters subgroup objects.')
pduOutputGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 3)).setObjects(("EATON-PDU-MIB", "pduOutputKilowattHours"), ("EATON-PDU-MIB", "pduOutputVA"), ("EATON-PDU-MIB", "pduOutputPower"), ("EATON-PDU-MIB", "pduOutputPowerFactor"), ("EATON-PDU-MIB", "pduNeutralCurrent"), ("EATON-PDU-MIB", "pduRatedOutputCurrent"), ("EATON-PDU-MIB", "pduOutputVoltageUnits"), ("EATON-PDU-MIB", "pduOutputNumPhases"), ("EATON-PDU-MIB", "pduOutputPhaseVoltage"), ("EATON-PDU-MIB", "pduOutputPhaseCurrent"), ("EATON-PDU-MIB", "pduOutputPhasePercentLoad"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pduOutputGroup = pduOutputGroup.setStatus('current')
if mibBuilder.loadTexts: pduOutputGroup.setDescription('The pduOutput Meters subgroup objects.')
panelRatingsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 4)).setObjects(("EATON-PDU-MIB", "panelRatedVoltage"), ("EATON-PDU-MIB", "panelRatedBreakerCurrent"), ("EATON-PDU-MIB", "panelNumPhases"), ("EATON-PDU-MIB", "panelNumBreakers"), ("EATON-PDU-MIB", "panelVoltageUnits"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    panelRatingsGroup = panelRatingsGroup.setStatus('current')
if mibBuilder.loadTexts: panelRatingsGroup.setDescription('The panelRatings table objects.')
panelMetersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 5)).setObjects(("EATON-PDU-MIB", "panelTotalKilowattHours"), ("EATON-PDU-MIB", "panelMonthlyKilowattHours"), ("EATON-PDU-MIB", "panelYtdKilowattHours"), ("EATON-PDU-MIB", "panelVA"), ("EATON-PDU-MIB", "panelPower"), ("EATON-PDU-MIB", "panelPowerFactor"), ("EATON-PDU-MIB", "panelNeutralCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    panelMetersGroup = panelMetersGroup.setStatus('current')
if mibBuilder.loadTexts: panelMetersGroup.setDescription('The BreakerMeters Table objects.')
panelPhaseMetersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 6)).setObjects(("EATON-PDU-MIB", "panelPhaseVoltage"), ("EATON-PDU-MIB", "panelPhaseCurrent"), ("EATON-PDU-MIB", "panelPhasePercentLoad"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    panelPhaseMetersGroup = panelPhaseMetersGroup.setStatus('current')
if mibBuilder.loadTexts: panelPhaseMetersGroup.setDescription('The BreakerPhaseMeters Table objects.')
breakerRatingsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 7)).setObjects(("EATON-PDU-MIB", "breakerName"), ("EATON-PDU-MIB", "breakerRatedCurrent"), ("EATON-PDU-MIB", "breakerNumPhases"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    breakerRatingsGroup = breakerRatingsGroup.setStatus('current')
if mibBuilder.loadTexts: breakerRatingsGroup.setDescription('The breakerRatings table objects.')
breakerMetersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 8)).setObjects(("EATON-PDU-MIB", "breakerTotalKilowattHours"), ("EATON-PDU-MIB", "breakerMonthlyKilowattHours"), ("EATON-PDU-MIB", "breakerYtdKilowattHours"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    breakerMetersGroup = breakerMetersGroup.setStatus('current')
if mibBuilder.loadTexts: breakerMetersGroup.setDescription('The breakerMeters table objects.')
breakerPhaseMetersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 9)).setObjects(("EATON-PDU-MIB", "breakerPhaseVA"), ("EATON-PDU-MIB", "breakerPhasePower"), ("EATON-PDU-MIB", "breakerPhasePowerFactor"), ("EATON-PDU-MIB", "breakerPhaseCurrent"), ("EATON-PDU-MIB", "breakerPhasePercentLoad"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    breakerPhaseMetersGroup = breakerPhaseMetersGroup.setStatus('current')
if mibBuilder.loadTexts: breakerPhaseMetersGroup.setDescription('The breakerPhaseMeters table objects.')
pdu3phaseCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 10)).setObjects(("EATON-PDU-MIB", "pduNameplateGroup"), ("EATON-PDU-MIB", "pduInputGroup"), ("EATON-PDU-MIB", "pduOutputGroup"), ("EATON-PDU-MIB", "panelRatingsGroup"), ("EATON-PDU-MIB", "panelMetersGroup"), ("EATON-PDU-MIB", "panelPhaseMetersGroup"), ("EATON-PDU-MIB", "breakerRatingsGroup"), ("EATON-PDU-MIB", "breakerMetersGroup"), ("EATON-PDU-MIB", "breakerPhaseMetersGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdu3phaseCompliance = pdu3phaseCompliance.setStatus('current')
if mibBuilder.loadTexts: pdu3phaseCompliance.setDescription('The compliance statement for a normal 3-phase PDU, which implements the full set of objects.')
mibBuilder.exportSymbols("EATON-PDU-MIB", panelTotalKilowattHours=panelTotalKilowattHours, pduNumPhases=pduNumPhases, breakerName=breakerName, eatonPduMIBObjects=eatonPduMIBObjects, pduInputGroup=pduInputGroup, pduInputVA=pduInputVA, pduInputNumPhases=pduInputNumPhases, panelVA=panelVA, panelMetersGroup=panelMetersGroup, pduBreaker=pduBreaker, panelNumBreakers=panelNumBreakers, PositiveInteger=PositiveInteger, pduInputPhasePercentLoad=pduInputPhasePercentLoad, breakerPhaseMetersEntry=breakerPhaseMetersEntry, pduOutputPowerFactor=pduOutputPowerFactor, panelMonthlyKilowattHours=panelMonthlyKilowattHours, breakerPhaseIndex=breakerPhaseIndex, pduInput=pduInput, pduNameplate=pduNameplate, eatonPduConformance=eatonPduConformance, panelPhaseMetersEntry=panelPhaseMetersEntry, pduInputPhaseVoltage=pduInputPhaseVoltage, pduOutputVA=pduOutputVA, panelPowerFactor=panelPowerFactor, pduOutputNumPhases=pduOutputNumPhases, breakerMonthlyKilowattHours=breakerMonthlyKilowattHours, eatonPduMIB=eatonPduMIB, panelRatingsTable=panelRatingsTable, breakerRatedCurrent=breakerRatedCurrent, breakerPhaseMetersTable=breakerPhaseMetersTable, panelPhaseVoltage=panelPhaseVoltage, panelMetersEntry=panelMetersEntry, panelVoltageUnits=panelVoltageUnits, panelPhasePercentLoad=panelPhasePercentLoad, breakerNumber=breakerNumber, pduNeutralCurrent=pduNeutralCurrent, breakerPhasePercentLoad=breakerPhasePercentLoad, pduNumPanels=pduNumPanels, pduGroundCurrent=pduGroundCurrent, pduOutputPhaseVoltage=pduOutputPhaseVoltage, NonNegativeInteger=NonNegativeInteger, panelPhaseMetersGroup=panelPhaseMetersGroup, pdu3phaseCompliance=pdu3phaseCompliance, panelYtdKilowattHours=panelYtdKilowattHours, breakerYtdKilowattHours=breakerYtdKilowattHours, breakerMetersTable=breakerMetersTable, panelRatingsGroup=panelRatingsGroup, panelMetersTable=panelMetersTable, breakerPhasePower=breakerPhasePower, breakerNumPhases=breakerNumPhases, pduOutputPhasePercentLoad=pduOutputPhasePercentLoad, pduOutputEntry=pduOutputEntry, mainPdu=mainPdu, panelPower=panelPower, panelPhaseCurrent=panelPhaseCurrent, pduInputTable=pduInputTable, panelNeutralCurrent=panelNeutralCurrent, panelRatedBreakerCurrent=panelRatedBreakerCurrent, breakerRatingsEntry=breakerRatingsEntry, breakerRatingsTable=breakerRatingsTable, panelRatedVoltage=panelRatedVoltage, breakerMetersEntry=breakerMetersEntry, pduPanel=pduPanel, pduRatedOutputCurrent=pduRatedOutputCurrent, pduInputEntry=pduInputEntry, breakerPhaseCurrent=breakerPhaseCurrent, panelRatingsEntry=panelRatingsEntry, pduInputVoltageUnits=pduInputVoltageUnits, panelPhaseMetersTable=panelPhaseMetersTable, breakerPhaseVA=breakerPhaseVA, pduInputPower=pduInputPower, PYSNMP_MODULE_ID=eatonPduMIB, breakerPhasePowerFactor=breakerPhasePowerFactor, pduInputPowerFactor=pduInputPowerFactor, pduOutputPhaseCurrent=pduOutputPhaseCurrent, pduOutputVoltageUnits=pduOutputVoltageUnits, pduInputPhaseIndex=pduInputPhaseIndex, breakerTotalKilowattHours=breakerTotalKilowattHours, breakerPhaseMetersGroup=breakerPhaseMetersGroup, pduInputPhaseCurrent=pduInputPhaseCurrent, breakerMetersGroup=breakerMetersGroup, pduOutputTable=pduOutputTable, panelNumber=panelNumber, pduRatingVA=pduRatingVA, breakerRatingsGroup=breakerRatingsGroup, pduOutputPhaseIndex=pduOutputPhaseIndex, pduOutputPower=pduOutputPower, pduOutputGroup=pduOutputGroup, panelNumPhases=panelNumPhases, pduNominalOutputVoltage=pduNominalOutputVoltage, pduFrequency=pduFrequency, pduOutput=pduOutput, pduNameplateGroup=pduNameplateGroup, pduOutputKilowattHours=pduOutputKilowattHours, panelPhaseIndex=panelPhaseIndex)
