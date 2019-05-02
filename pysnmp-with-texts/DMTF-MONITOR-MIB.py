#
# PySNMP MIB module DMTF-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DMTF-MONITOR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:51:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
dmiCompId, dmiEventSystem, dmiEventDateTime, DmiString, dmiEventSubSystem, dmiEventStateKey, dmiEventSeverity, dmiEventAssociatedGroup = mibBuilder.importSymbols("DMTF-DMI-MIB", "dmiCompId", "dmiEventSystem", "dmiEventDateTime", "DmiString", "dmiEventSubSystem", "dmiEventStateKey", "dmiEventSeverity", "dmiEventAssociatedGroup")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, TimeTicks, IpAddress, Gauge32, iso, ModuleIdentity, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, Counter64, NotificationType, enterprises, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "IpAddress", "Gauge32", "iso", "ModuleIdentity", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "Counter64", "NotificationType", "enterprises", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DmiCounter(Counter32):
    pass

class DmiCounter64(Counter64):
    pass

class DmiGauge(Gauge32):
    pass

class DmiInteger(Integer32):
    pass

class DmiOctetstring(OctetString):
    pass

class DmiCompId(Integer32):
    pass

class DmiGroupId(Integer32):
    pass

dmtf = MibIdentifier((1, 3, 6, 1, 4, 1, 412))
dmtfStdMifs = MibIdentifier((1, 3, 6, 1, 4, 1, 412, 2))
dmtfDynOids = MibIdentifier((1, 3, 6, 1, 4, 1, 412, 3))
dmtfMonitorMIF = ModuleIdentity((1, 3, 6, 1, 4, 1, 412, 2, 6))
if mibBuilder.loadTexts: dmtfMonitorMIF.setLastUpdated('9710221800Z')
if mibBuilder.loadTexts: dmtfMonitorMIF.setOrganization('Desktop Management Task Force')
if mibBuilder.loadTexts: dmtfMonitorMIF.setContactInfo(' DMTF Technical Advisory Committee Mailstop JF2-53 2111 N.E. 25th Avenue Hillsboro, OR 97124 Phone: +1 503 264-9300 Email: dmtf-info@dmtf.org ')
if mibBuilder.loadTexts: dmtfMonitorMIF.setDescription('This MIB is a translation of the DMTF Monitor MIF based on the translation rules defined by the DMTF DMI to SNMP Mapping Standard, Version 1.0. DMI-based systems running a DMI-to-SNMP Mapping Agent provide the ability to access DMI component instrumentation via SNMP protocol operations. ')
dmtfMonitorAdditionalInformationsTable = MibTable((1, 3, 6, 1, 4, 1, 412, 2, 6, 1), )
if mibBuilder.loadTexts: dmtfMonitorAdditionalInformationsTable.setStatus('current')
if mibBuilder.loadTexts: dmtfMonitorAdditionalInformationsTable.setDescription('This group gives more informations about this monitor.')
dmtfMonitorAdditionalInformationsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 412, 2, 6, 1, 1), ).setIndexNames((0, "DMTF-MONITOR-MIB", "DmiCompId"), (0, "DMTF-MONITOR-MIB", "DmiGroupId"))
if mibBuilder.loadTexts: dmtfMonitorAdditionalInformationsEntry.setStatus('current')
if mibBuilder.loadTexts: dmtfMonitorAdditionalInformationsEntry.setDescription('This group gives more informations about this monitor.')
assetTag = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 1, 1, 1), DmiString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: assetTag.setReference("'DMTF|Monitor Additional Informations|001' 1")
if mibBuilder.loadTexts: assetTag.setStatus('current')
if mibBuilder.loadTexts: assetTag.setDescription('The monitor asset tag number')
monitorLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 1, 1, 2), DmiString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: monitorLocation.setReference("'DMTF|Monitor Additional Informations|001' 2")
if mibBuilder.loadTexts: monitorLocation.setStatus('current')
if mibBuilder.loadTexts: monitorLocation.setDescription('The physical location of this monitor')
monitorPrimaryUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 1, 1, 3), DmiString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: monitorPrimaryUserName.setReference("'DMTF|Monitor Additional Informations|001' 3")
if mibBuilder.loadTexts: monitorPrimaryUserName.setStatus('current')
if mibBuilder.loadTexts: monitorPrimaryUserName.setDescription('The name of the primary user or owner of this monitor')
monitorPrimaryUserPhone = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 1, 1, 4), DmiString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: monitorPrimaryUserPhone.setReference("'DMTF|Monitor Additional Informations|001' 4")
if mibBuilder.loadTexts: monitorPrimaryUserPhone.setStatus('current')
if mibBuilder.loadTexts: monitorPrimaryUserPhone.setDescription('the phone number of the primary user of this monitor')
dmtfMonitorResolutionsTable = MibTable((1, 3, 6, 1, 4, 1, 412, 2, 6, 2), )
if mibBuilder.loadTexts: dmtfMonitorResolutionsTable.setStatus('current')
if mibBuilder.loadTexts: dmtfMonitorResolutionsTable.setDescription('This group defines all the resolutions supported by this monitor')
dmtfMonitorResolutionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1), ).setIndexNames((0, "DMTF-MONITOR-MIB", "DmiCompId"), (0, "DMTF-MONITOR-MIB", "DmiGroupId"), (0, "DMTF-MONITOR-MIB", "monitorResolutionIndex"))
if mibBuilder.loadTexts: dmtfMonitorResolutionsEntry.setStatus('current')
if mibBuilder.loadTexts: dmtfMonitorResolutionsEntry.setDescription('This group defines all the resolutions supported by this monitor')
dmtfMonitorResolutionsState = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 0), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtfMonitorResolutionsState.setReference("'DMTF|Monitor Resolutions|002' 0")
if mibBuilder.loadTexts: dmtfMonitorResolutionsState.setStatus('current')
monitorResolutionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 1), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monitorResolutionIndex.setReference("'DMTF|Monitor Resolutions|002' 1")
if mibBuilder.loadTexts: monitorResolutionIndex.setStatus('current')
if mibBuilder.loadTexts: monitorResolutionIndex.setDescription('This is an index into the Monitor Resolution table.')
horizontalResolution = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 2), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: horizontalResolution.setReference("'DMTF|Monitor Resolutions|002' 2")
if mibBuilder.loadTexts: horizontalResolution.setStatus('current')
if mibBuilder.loadTexts: horizontalResolution.setDescription('Horizontal Resolution value in pixels')
verticalResolution = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 3), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: verticalResolution.setReference("'DMTF|Monitor Resolutions|002' 3")
if mibBuilder.loadTexts: verticalResolution.setStatus('current')
if mibBuilder.loadTexts: verticalResolution.setDescription('Vertical Resolution value in pixels')
refreshRate = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 4), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: refreshRate.setReference("'DMTF|Monitor Resolutions|002' 4")
if mibBuilder.loadTexts: refreshRate.setStatus('current')
if mibBuilder.loadTexts: refreshRate.setDescription('Refresh Rate value for this resolution in Hz')
verticalScanMode = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("unknown", 2), ("unsupported", 3), ("notInterlaced", 4), ("interlaced", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: verticalScanMode.setReference("'DMTF|Monitor Resolutions|002' 5")
if mibBuilder.loadTexts: verticalScanMode.setStatus('current')
if mibBuilder.loadTexts: verticalScanMode.setDescription('Vertical scan mode interlaced or not')
minimumMonitorRefreshRate = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 6), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: minimumMonitorRefreshRate.setReference("'DMTF|Monitor Resolutions|002' 6")
if mibBuilder.loadTexts: minimumMonitorRefreshRate.setStatus('current')
if mibBuilder.loadTexts: minimumMonitorRefreshRate.setDescription('Minimum refresh rate value for this resolution for monitors supporting a range of refresh rates.')
maximumMonitorRefreshRate = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 7), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maximumMonitorRefreshRate.setReference("'DMTF|Monitor Resolutions|002' 7")
if mibBuilder.loadTexts: maximumMonitorRefreshRate.setStatus('current')
if mibBuilder.loadTexts: maximumMonitorRefreshRate.setDescription('Maximum refresh rate value for this resolution for monitors supporting a range of refresh rates.')
mibBuilder.exportSymbols("DMTF-MONITOR-MIB", dmtfMonitorResolutionsState=dmtfMonitorResolutionsState, dmtfMonitorResolutionsEntry=dmtfMonitorResolutionsEntry, monitorLocation=monitorLocation, horizontalResolution=horizontalResolution, verticalResolution=verticalResolution, dmtfMonitorMIF=dmtfMonitorMIF, assetTag=assetTag, dmtf=dmtf, PYSNMP_MODULE_ID=dmtfMonitorMIF, dmtfMonitorAdditionalInformationsTable=dmtfMonitorAdditionalInformationsTable, DmiOctetstring=DmiOctetstring, DmiCompId=DmiCompId, monitorPrimaryUserName=monitorPrimaryUserName, verticalScanMode=verticalScanMode, refreshRate=refreshRate, minimumMonitorRefreshRate=minimumMonitorRefreshRate, DmiCounter=DmiCounter, dmtfStdMifs=dmtfStdMifs, DmiInteger=DmiInteger, DmiGauge=DmiGauge, DmiGroupId=DmiGroupId, DmiCounter64=DmiCounter64, dmtfMonitorAdditionalInformationsEntry=dmtfMonitorAdditionalInformationsEntry, dmtfMonitorResolutionsTable=dmtfMonitorResolutionsTable, monitorResolutionIndex=monitorResolutionIndex, monitorPrimaryUserPhone=monitorPrimaryUserPhone, maximumMonitorRefreshRate=maximumMonitorRefreshRate, dmtfDynOids=dmtfDynOids)
