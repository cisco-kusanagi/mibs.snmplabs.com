#
# PySNMP MIB module WCCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WCCP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:36:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, MibIdentifier, iso, IpAddress, TimeTicks, Counter64, NotificationType, ObjectIdentity, ModuleIdentity, Counter32, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "MibIdentifier", "iso", "IpAddress", "TimeTicks", "Counter64", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Counter32", "Bits", "Integer32")
TextualConvention, TimeStamp, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "DisplayString", "TruthValue")
deviceWccpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 5))
if mibBuilder.loadTexts: deviceWccpMIB.setLastUpdated('0208280300Z')
if mibBuilder.loadTexts: deviceWccpMIB.setOrganization('Blue Coat Systems, Inc.')
if mibBuilder.loadTexts: deviceWccpMIB.setContactInfo('support@bluecoat.com')
if mibBuilder.loadTexts: deviceWccpMIB.setDescription("The deviceWccpMIB is used to monitor the status of the device's WCCP.")
class WccpServiceType(TextualConvention, Integer32):
    description = 'Indicates the type of WCCP service being used. standard standard or well known service is being used. dynamic dynamic service is being used. unknown cannot determine the type of service being used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("standard", 1), ("dynamic", 2), ("unknown", 3))

class WccpVersion(TextualConvention, Integer32):
    description = 'Indicates the version of WCCP being used for a service. version1 WCCP version 1 being used for the service. version2 WCCP version 2 being used for the service. unknown unknown version.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("version1", 1), ("version2", 2), ("unknown", 3))

deviceWccpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 5, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpEnabled.setStatus('current')
if mibBuilder.loadTexts: deviceWccpEnabled.setDescription('This variable show whether WCCP is enabled or not.')
deviceWccpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2))
deviceWccpValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1))
deviceWccpValueTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1), )
if mibBuilder.loadTexts: deviceWccpValueTable.setStatus('current')
if mibBuilder.loadTexts: deviceWccpValueTable.setDescription('Table of WCCP services.')
deviceWccpValueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1), ).setIndexNames((0, "WCCP-MIB", "deviceWccpIndex"))
if mibBuilder.loadTexts: deviceWccpValueEntry.setStatus('current')
if mibBuilder.loadTexts: deviceWccpValueEntry.setDescription('A deviceWccpValueTable entry describes the status of a WCCP service.')
deviceWccpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: deviceWccpIndex.setStatus('current')
if mibBuilder.loadTexts: deviceWccpIndex.setDescription('An arbitrary value which uniquely identifies the WCCP service.')
deviceWccpServiceID = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpServiceID.setStatus('current')
if mibBuilder.loadTexts: deviceWccpServiceID.setDescription("This variable indicates WCCP's service id.")
deviceWccpServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 3), WccpServiceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpServiceType.setStatus('current')
if mibBuilder.loadTexts: deviceWccpServiceType.setDescription("This variable indicates WCCP's service type.")
deviceWccpServiceVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 4), WccpVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpServiceVersion.setStatus('current')
if mibBuilder.loadTexts: deviceWccpServiceVersion.setDescription("This variable indicates the WCCP service's version.")
deviceWccpPacketsRedir = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpPacketsRedir.setStatus('current')
if mibBuilder.loadTexts: deviceWccpPacketsRedir.setDescription('This variable indicates the how many WCCP packets have been redirected.')
deviceWccpPacketsLowRedir = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpPacketsLowRedir.setStatus('current')
if mibBuilder.loadTexts: deviceWccpPacketsLowRedir.setDescription('This variable indicates the how many WCCP packets have been redirected - lower 32 bits.')
deviceWccpBytesRedir = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpBytesRedir.setStatus('current')
if mibBuilder.loadTexts: deviceWccpBytesRedir.setDescription('This variable indicates how many WCCP bytes have been redirected.')
deviceWccpBytesLowRedir = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpBytesLowRedir.setStatus('current')
if mibBuilder.loadTexts: deviceWccpBytesLowRedir.setDescription('This variable indicates how many WCCP bytes have been redirected - lower 32 bits.')
mibBuilder.exportSymbols("WCCP-MIB", deviceWccpServiceVersion=deviceWccpServiceVersion, deviceWccpMIB=deviceWccpMIB, deviceWccpServiceID=deviceWccpServiceID, WccpServiceType=WccpServiceType, deviceWccpBytesRedir=deviceWccpBytesRedir, deviceWccpMIBObjects=deviceWccpMIBObjects, WccpVersion=WccpVersion, deviceWccpValueTable=deviceWccpValueTable, deviceWccpBytesLowRedir=deviceWccpBytesLowRedir, deviceWccpPacketsLowRedir=deviceWccpPacketsLowRedir, deviceWccpIndex=deviceWccpIndex, deviceWccpEnabled=deviceWccpEnabled, deviceWccpValueEntry=deviceWccpValueEntry, deviceWccpPacketsRedir=deviceWccpPacketsRedir, deviceWccpServiceType=deviceWccpServiceType, PYSNMP_MODULE_ID=deviceWccpMIB, deviceWccpValues=deviceWccpValues)
