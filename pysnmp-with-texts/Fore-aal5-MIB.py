#
# PySNMP MIB module Fore-aal5-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-aal5-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:17:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
frameInternetworking, = mibBuilder.importSymbols("Fore-Common-MIB", "frameInternetworking")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, IpAddress, Unsigned32, TimeTicks, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, Counter64, Counter32, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "IpAddress", "Unsigned32", "TimeTicks", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "Counter64", "Counter32", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aal5 = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 1, 16, 5))
if mibBuilder.loadTexts: aal5.setLastUpdated('9706100906Z')
if mibBuilder.loadTexts: aal5.setOrganization('FORE')
if mibBuilder.loadTexts: aal5.setContactInfo(' Postal: FORE Systems Inc. 1000 FORE Drive Warrendale, PA 15086-7502 Tel: +1 724 742 6900 Email: nm_mibs@fore.com Web: http://www.fore.com')
if mibBuilder.loadTexts: aal5.setDescription('This MIB module defines the FORE Systems AAL5 and EPD/PPD management interface of the Mercury netmod (FUNI FR/ATM interworking )')
aal5VccTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1), )
if mibBuilder.loadTexts: aal5VccTable.setStatus('current')
if mibBuilder.loadTexts: aal5VccTable.setDescription('This table contains AAL5 VCC performance parameters.')
aal5VccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1), ).setIndexNames((0, "Fore-aal5-MIB", "aal5VccAtmFabServiceIfIndex"), (0, "Fore-aal5-MIB", "aal5VccFabVpi"), (0, "Fore-aal5-MIB", "aal5VccFabVci"))
if mibBuilder.loadTexts: aal5VccEntry.setStatus('current')
if mibBuilder.loadTexts: aal5VccEntry.setDescription('This list contains the AAL5 VCC performance parameters. Entries in this table are indexed by ifIndex assigned to this interface and vpi/vci pairs assigned to this connection by either provisioning or signalling. Since this entry is associated with the netmod/fabric interface, indexes are fabric VPI/VCI and fabric service if index')
aal5VccAtmFabServiceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccAtmFabServiceIfIndex.setStatus('current')
if mibBuilder.loadTexts: aal5VccAtmFabServiceIfIndex.setDescription('ifIndex assigned to this interface.')
aal5VccFabVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccFabVpi.setStatus('current')
if mibBuilder.loadTexts: aal5VccFabVpi.setDescription('vpi assigned to this interface.')
aal5VccFabVci = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccFabVci.setStatus('current')
if mibBuilder.loadTexts: aal5VccFabVci.setDescription('vci assigned to this interface.')
aal5VccCrcErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccCrcErrs.setStatus('current')
if mibBuilder.loadTexts: aal5VccCrcErrs.setDescription('The number of AAL5 CPCS PDUs received with CRC-32 errors on this AAL5 VCC at the interface associated with this AAL5 entity.')
aal5VccSarTimeOuts = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccSarTimeOuts.setStatus('current')
if mibBuilder.loadTexts: aal5VccSarTimeOuts.setDescription(' The number of timeouts at the SAR level, waiting for a CPCS trailer')
aal5VccOverSizedPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccOverSizedPDUs.setStatus('current')
if mibBuilder.loadTexts: aal5VccOverSizedPDUs.setDescription('The number of AAL5 CPCS PDUs discarded on this ATM VCC at the interface associated with an AAL5 entity due to the AAL5 PDUs being too large.')
aal5VccLengthErrPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccLengthErrPDUs.setStatus('current')
if mibBuilder.loadTexts: aal5VccLengthErrPDUs.setDescription('The number of AAL5 CPCS PDUs discarded on this ATM VCC at the interface associated with an AAL5 entity due to the AAL5 PDU length errors.')
aal5VccCPIErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccCPIErrs.setStatus('current')
if mibBuilder.loadTexts: aal5VccCPIErrs.setDescription('The number of CPI ( Common Part Indicator ) current errors ')
aal5VccInPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccInPDUs.setStatus('current')
if mibBuilder.loadTexts: aal5VccInPDUs.setDescription("The number of AAL-5 PDU's transmitted by the interworking function on this ATM VCC.")
aal5VccOutPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccOutPDUs.setStatus('current')
if mibBuilder.loadTexts: aal5VccOutPDUs.setDescription("The number of AAL-5 PDU's received by the interworking function on this ATM VCC.")
aal5VccInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccInOctets.setStatus('current')
if mibBuilder.loadTexts: aal5VccInOctets.setDescription('The number of AAL-5 octets transmitted by the interworking function on this ATM VCC.')
aal5VccOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccOutOctets.setStatus('current')
if mibBuilder.loadTexts: aal5VccOutOctets.setDescription('The number of AAL-5 octets received by the interworking function on this ATM VCC.')
aal5CpcsCurrTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2), )
if mibBuilder.loadTexts: aal5CpcsCurrTable.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsCurrTable.setDescription("This table holds current ( within the last 15 minutes interval's statistics of AAL5 CPCS sublayer")
aal5CpcsCurrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2, 1), ).setIndexNames((0, "Fore-aal5-MIB", "aal5CpcsFabServiceIfIndex"))
if mibBuilder.loadTexts: aal5CpcsCurrEntry.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsCurrEntry.setDescription('Entry in the table of current statistics of AAL5 CPCS sublayer')
aal5CpcsFabServiceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsFabServiceIfIndex.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsFabServiceIfIndex.setDescription('ifIndex assigned to this entry.')
aal5CpcsCurrCRCErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsCurrCRCErrs.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsCurrCRCErrs.setDescription('The CRC current errors')
aal5CpcsCurrSarTimeOuts = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsCurrSarTimeOuts.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsCurrSarTimeOuts.setDescription('The current number of Timeouts in the CPCS level, waiting for a CPCS trailer ')
aal5CpcsCurrOverSizedPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsCurrOverSizedPDUs.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsCurrOverSizedPDUs.setDescription('The User Payload current errors')
aal5CpcsCurrLengthErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsCurrLengthErrs.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsCurrLengthErrs.setDescription('The Length current errors')
aal5CpcsCurrCPIErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsCurrCPIErrs.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsCurrCPIErrs.setDescription('The CPI ( Common Part Indicator ) current errors ')
aal5CpcsIntvlTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3), )
if mibBuilder.loadTexts: aal5CpcsIntvlTable.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsIntvlTable.setDescription('This table holds interval statistics of AAL5 CPCS sublayer for 8 hour worth 15 minutes intervals. The table is indexed by the service ifIndex as well as interval number in range of 1..32')
aal5CpcsIntvlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1), ).setIndexNames((0, "Fore-aal5-MIB", "aal5CpcsIntvlFabServiceIfIndex"), (0, "Fore-aal5-MIB", "aal5CpcsIntvlNumber"))
if mibBuilder.loadTexts: aal5CpcsIntvlEntry.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsIntvlEntry.setDescription('Entry in the table of interval statistics of AAL5 CPCS sublayer')
aal5CpcsIntvlFabServiceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsIntvlFabServiceIfIndex.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsIntvlFabServiceIfIndex.setDescription('ifIndex assigned to this entry.')
aal5CpcsIntvlNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsIntvlNumber.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsIntvlNumber.setDescription('A number between 1 and 32, where 1 is the most recently completed 15 minute interval and 32 is the least recently completed 15 minutes interval ( assuming that all 32 intervals are valid ) .')
aal5CpcsIntvlCRCErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsIntvlCRCErrs.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsIntvlCRCErrs.setDescription('The CRC interval errors')
aal5CpcsIntvlSarTimeOuts = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsIntvlSarTimeOuts.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsIntvlSarTimeOuts.setDescription('The interval number of Timeouts in the CPCS level, waiting for a CPCS trailer ')
aal5CpcsIntvlOverSizedPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsIntvlOverSizedPDUs.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsIntvlOverSizedPDUs.setDescription('The User Payload interval errors')
aal5CpcsIntvlLengthErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsIntvlLengthErrs.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsIntvlLengthErrs.setDescription('The Length interval errors')
aal5CpcsIntvlCPIErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsIntvlCPIErrs.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsIntvlCPIErrs.setDescription('The CPI ( Common Part Indicator ) interval errors ')
aal5CpcsTotalTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4), )
if mibBuilder.loadTexts: aal5CpcsTotalTable.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsTotalTable.setDescription('This table holds cumulative statistics of AAL5 CPCS sublayer')
aal5CpcsTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1), ).setIndexNames((0, "Fore-aal5-MIB", "aal5CpcsTotalFabServiceIfIndex"))
if mibBuilder.loadTexts: aal5CpcsTotalEntry.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsTotalEntry.setDescription('Entry in the table of cumulative statistics of AAL5 CPCS sublayer')
aal5CpcsTotalFabServiceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsTotalFabServiceIfIndex.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsTotalFabServiceIfIndex.setDescription('ifIndex assigned to this entry.')
aal5CpcsTotalValidIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsTotalValidIntervals.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsTotalValidIntervals.setDescription('The number of previous intervals for which valid data was collected. The value will be 32 unless the interface was brought on-line within the last 8 hours, in which case the value will be the number of complete 15 minute intervals since the interface has been online.')
aal5CpcsTotalCRCErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsTotalCRCErrs.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsTotalCRCErrs.setDescription('The CRC total errors')
aal5CpcsTotalSarTimeOuts = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsTotalSarTimeOuts.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsTotalSarTimeOuts.setDescription('The total number of Timeouts in the CPCS level, waiting for a CPCS trailer ')
aal5CpcsTotalOverSizedPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsTotalOverSizedPDUs.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsTotalOverSizedPDUs.setDescription('The User Payload total errors')
aal5CpcsTotalLengthErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsTotalLengthErrs.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsTotalLengthErrs.setDescription('The Length total errors')
aal5CpcsTotalCPIErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsTotalCPIErrs.setStatus('current')
if mibBuilder.loadTexts: aal5CpcsTotalCPIErrs.setDescription('The CPI ( Common Part Indicator ) total errors ')
aal5EpdPpdVccTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5), )
if mibBuilder.loadTexts: aal5EpdPpdVccTable.setStatus('current')
if mibBuilder.loadTexts: aal5EpdPpdVccTable.setDescription('A table of statistical information associated with the EPD/PPD controller on a per connection basis.')
aal5EpdPpdVccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1), ).setIndexNames((0, "Fore-aal5-MIB", "aal5EpdPpdAtmFabServiceIfIndex"), (0, "Fore-aal5-MIB", "aal5EpdPpdVccFabVpi"), (0, "Fore-aal5-MIB", "aal5EpdPpdVccFabVci"))
if mibBuilder.loadTexts: aal5EpdPpdVccEntry.setStatus('current')
if mibBuilder.loadTexts: aal5EpdPpdVccEntry.setDescription('An entry in the FRAM netmod EPD/PPD statistic information table on a per connection basis')
aal5EpdPpdAtmFabServiceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5EpdPpdAtmFabServiceIfIndex.setStatus('current')
if mibBuilder.loadTexts: aal5EpdPpdAtmFabServiceIfIndex.setDescription('ifIndex assigned to this entry.')
aal5EpdPpdVccFabVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5EpdPpdVccFabVpi.setStatus('current')
if mibBuilder.loadTexts: aal5EpdPpdVccFabVpi.setDescription('vpi assigned to this entry.')
aal5EpdPpdVccFabVci = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5EpdPpdVccFabVci.setStatus('current')
if mibBuilder.loadTexts: aal5EpdPpdVccFabVci.setDescription('vci assigned to this entry.')
aal5EpdPpdVccDroppedCellsClp1 = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5EpdPpdVccDroppedCellsClp1.setStatus('current')
if mibBuilder.loadTexts: aal5EpdPpdVccDroppedCellsClp1.setDescription('The total number of dropped cells with CLP=1 by the EPD/PPD controller for a specific connection')
aal5EpdPpdVccForwardedCellsClp1 = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5EpdPpdVccForwardedCellsClp1.setStatus('current')
if mibBuilder.loadTexts: aal5EpdPpdVccForwardedCellsClp1.setDescription('The total number of forwarded cells with CLP=1 by the EPD/PPD controller for a specific connection')
aal5EpdPpdVccDroppedCellsClp0 = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5EpdPpdVccDroppedCellsClp0.setStatus('current')
if mibBuilder.loadTexts: aal5EpdPpdVccDroppedCellsClp0.setDescription('The total number of dropped cells with CLP=0 by the EPD/PPD controller for a specific connection')
aal5EpdPpdVccForwardedCellsClp0 = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5EpdPpdVccForwardedCellsClp0.setStatus('current')
if mibBuilder.loadTexts: aal5EpdPpdVccForwardedCellsClp0.setDescription('The total number of forwarded cells with CLP=0 by the EPD/PPD controller for a specific connection')
mibBuilder.exportSymbols("Fore-aal5-MIB", aal5CpcsTotalValidIntervals=aal5CpcsTotalValidIntervals, aal5CpcsTotalCPIErrs=aal5CpcsTotalCPIErrs, aal5CpcsCurrEntry=aal5CpcsCurrEntry, aal5CpcsIntvlNumber=aal5CpcsIntvlNumber, aal5VccInPDUs=aal5VccInPDUs, aal5VccCPIErrs=aal5VccCPIErrs, aal5VccCrcErrs=aal5VccCrcErrs, aal5EpdPpdVccDroppedCellsClp1=aal5EpdPpdVccDroppedCellsClp1, aal5CpcsCurrTable=aal5CpcsCurrTable, aal5VccFabVpi=aal5VccFabVpi, aal5=aal5, aal5CpcsIntvlTable=aal5CpcsIntvlTable, aal5CpcsTotalOverSizedPDUs=aal5CpcsTotalOverSizedPDUs, aal5EpdPpdVccEntry=aal5EpdPpdVccEntry, aal5EpdPpdVccTable=aal5EpdPpdVccTable, aal5CpcsCurrLengthErrs=aal5CpcsCurrLengthErrs, aal5CpcsTotalEntry=aal5CpcsTotalEntry, aal5EpdPpdVccFabVpi=aal5EpdPpdVccFabVpi, aal5EpdPpdAtmFabServiceIfIndex=aal5EpdPpdAtmFabServiceIfIndex, aal5CpcsIntvlEntry=aal5CpcsIntvlEntry, aal5VccOverSizedPDUs=aal5VccOverSizedPDUs, aal5EpdPpdVccForwardedCellsClp1=aal5EpdPpdVccForwardedCellsClp1, aal5CpcsIntvlLengthErrs=aal5CpcsIntvlLengthErrs, aal5CpcsTotalSarTimeOuts=aal5CpcsTotalSarTimeOuts, aal5EpdPpdVccFabVci=aal5EpdPpdVccFabVci, aal5VccTable=aal5VccTable, aal5CpcsCurrOverSizedPDUs=aal5CpcsCurrOverSizedPDUs, aal5CpcsIntvlOverSizedPDUs=aal5CpcsIntvlOverSizedPDUs, aal5CpcsCurrSarTimeOuts=aal5CpcsCurrSarTimeOuts, aal5CpcsTotalFabServiceIfIndex=aal5CpcsTotalFabServiceIfIndex, aal5VccAtmFabServiceIfIndex=aal5VccAtmFabServiceIfIndex, aal5CpcsIntvlSarTimeOuts=aal5CpcsIntvlSarTimeOuts, aal5CpcsIntvlCRCErrs=aal5CpcsIntvlCRCErrs, aal5CpcsTotalTable=aal5CpcsTotalTable, aal5CpcsCurrCPIErrs=aal5CpcsCurrCPIErrs, aal5CpcsCurrCRCErrs=aal5CpcsCurrCRCErrs, aal5EpdPpdVccDroppedCellsClp0=aal5EpdPpdVccDroppedCellsClp0, aal5CpcsFabServiceIfIndex=aal5CpcsFabServiceIfIndex, aal5CpcsIntvlCPIErrs=aal5CpcsIntvlCPIErrs, aal5VccLengthErrPDUs=aal5VccLengthErrPDUs, aal5VccEntry=aal5VccEntry, aal5VccInOctets=aal5VccInOctets, aal5CpcsTotalLengthErrs=aal5CpcsTotalLengthErrs, PYSNMP_MODULE_ID=aal5, aal5EpdPpdVccForwardedCellsClp0=aal5EpdPpdVccForwardedCellsClp0, aal5CpcsTotalCRCErrs=aal5CpcsTotalCRCErrs, aal5VccSarTimeOuts=aal5VccSarTimeOuts, aal5VccOutOctets=aal5VccOutOctets, aal5VccOutPDUs=aal5VccOutPDUs, aal5VccFabVci=aal5VccFabVci, aal5CpcsIntvlFabServiceIfIndex=aal5CpcsIntvlFabServiceIfIndex)
