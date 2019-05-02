#
# PySNMP MIB module ASCEND-RESOURCES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-RESOURCES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:29:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
resourcesGroup, = mibBuilder.importSymbols("ASCEND-MIB", "resourcesGroup")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ObjectIdentity, Counter64, Unsigned32, MibIdentifier, ModuleIdentity, Counter32, NotificationType, Gauge32, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "Counter64", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Counter32", "NotificationType", "Gauge32", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
resourceUsageTable = MibTable((1, 3, 6, 1, 4, 1, 529, 27, 1), )
if mibBuilder.loadTexts: resourceUsageTable.setStatus('mandatory')
if mibBuilder.loadTexts: resourceUsageTable.setDescription('A list of slot entries that report their resources usage.')
resourceUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 27, 1, 1), ).setIndexNames((0, "ASCEND-RESOURCES-MIB", "usageSlotIndex"))
if mibBuilder.loadTexts: resourceUsageEntry.setStatus('mandatory')
if mibBuilder.loadTexts: resourceUsageEntry.setDescription('A list of entries that contain information about resource usage such as available,busy, suspect, disabled, dead.')
usageSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 27, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usageSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: usageSlotIndex.setDescription('A unique value for each slot in the system. The slot identified by a particular value of this index is the same slot as identified by the same value of slotIndex.')
usageAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 27, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usageAvailable.setStatus('mandatory')
if mibBuilder.loadTexts: usageAvailable.setDescription('The number of resources in this slot that are available to be assigned for incoming/outgoing calls.')
usageBusy = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 27, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usageBusy.setStatus('mandatory')
if mibBuilder.loadTexts: usageBusy.setDescription('The number of resources in this slot that are currently being assigned for incoming/outgoing calls.')
usageSuspect = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 27, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usageSuspect.setStatus('mandatory')
if mibBuilder.loadTexts: usageSuspect.setDescription('The number of resources in this slot that are in suspect state. They are tried after resources in the available pool are exhausted.')
usageDisabled = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 27, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usageDisabled.setStatus('mandatory')
if mibBuilder.loadTexts: usageDisabled.setDescription('The number of resources in this slot that are administratively disabled. Resources in disabled pool will not be assigned for incoming/outgoing calls.')
usageDead = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 27, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usageDead.setStatus('mandatory')
if mibBuilder.loadTexts: usageDead.setDescription('The number of resources in this slot taht are in fault state. Resources in dead pool will not be assigned for incoming/outgoing calls.')
resourceTable = MibTable((1, 3, 6, 1, 4, 1, 529, 27, 2), )
if mibBuilder.loadTexts: resourceTable.setStatus('mandatory')
if mibBuilder.loadTexts: resourceTable.setDescription('A list of individual terminating resource items.')
resourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 27, 2, 1), ).setIndexNames((0, "ASCEND-RESOURCES-MIB", "resourceSlotIndex"), (0, "ASCEND-RESOURCES-MIB", "resourcePortIndex"))
if mibBuilder.loadTexts: resourceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: resourceEntry.setDescription('Entry holding information about an individual item properties.')
resourceSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 27, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: resourceSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: resourceSlotIndex.setDescription('A unique value for each slot in the system. The slot identified by a particular value of this index is the same slot as identified by the same value of slotIndex.')
resourcePortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 27, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: resourcePortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: resourcePortIndex.setDescription('A unique value for each port/channel in each slot.')
resourceConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 27, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("enable", 2), ("disable", 3), ("disableAndChannel", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: resourceConfig.setStatus('mandatory')
if mibBuilder.loadTexts: resourceConfig.setDescription('The resource item configuration state. SETs are allowed only if the corresponding slot card adminstation state is enabled. Note: disableAndChannel(4) is the same as disable(3) and also disable one b-channel on a T1 line. This option is only available for modems in T1 network.')
resourceState = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 27, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("notApplicable", 1), ("other", 2), ("failedPost", 3), ("idle", 4), ("online", 5), ("virtualConnect", 6), ("disabled", 7), ("disabledChan", 8), ("reserved", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: resourceState.setStatus('mandatory')
if mibBuilder.loadTexts: resourceState.setDescription('The state of this resource item.')
resourceCallType = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 27, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("notApplicable", 1), ("other", 2), ("async", 3), ("sync", 4), ("isdnSync", 5), ("isdnAsyncV120", 6), ("isdnAsyncV110", 7), ("virtual", 8), ("isdnAsyncV32", 9), ("isdnAsyncVdsp", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: resourceCallType.setStatus('mandatory')
if mibBuilder.loadTexts: resourceCallType.setDescription('Type of calls is being served. If the resourceState variable is not online(5) or virtualConnect(6), this variable returns notApplicable(1). If the resourceState variable is online(5) or virtualConnect(6) and the type of call is not defined, this variable returns other(2) which indicates an unknown call type.')
resourceCallDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 27, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notApplicable", 1), ("other", 2), ("originated", 3), ("answered", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: resourceCallDirection.setStatus('mandatory')
if mibBuilder.loadTexts: resourceCallDirection.setDescription('Call direction associated with this item. If the resourceState variable is not online(5) or virtualConnect(6), this variable returns notApplicable(1). If the resourceState variable is online(5) or virtualConnect(6) and it is neither outgoing call nor incoming call, this variable returns none(2) which indicates an unknown call direction.')
resourceUsedCounts = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 27, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: resourceUsedCounts.setStatus('mandatory')
if mibBuilder.loadTexts: resourceUsedCounts.setDescription('The number of times this resource was utilized.')
resourceBadCounts = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 27, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: resourceBadCounts.setStatus('mandatory')
if mibBuilder.loadTexts: resourceBadCounts.setDescription('The number of times this resource failed.')
resourceLast32 = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 27, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: resourceLast32.setStatus('mandatory')
if mibBuilder.loadTexts: resourceLast32.setDescription("A 32-bit mask of the last 32 times this resource was tried. A '0' in the bit position indicates failure while a '1' indicates success.")
mibBuilder.exportSymbols("ASCEND-RESOURCES-MIB", resourceState=resourceState, usageAvailable=usageAvailable, usageSuspect=usageSuspect, resourceTable=resourceTable, resourceBadCounts=resourceBadCounts, resourceUsageTable=resourceUsageTable, resourceLast32=resourceLast32, resourcePortIndex=resourcePortIndex, resourceCallType=resourceCallType, resourceCallDirection=resourceCallDirection, usageSlotIndex=usageSlotIndex, usageDead=usageDead, resourceUsedCounts=resourceUsedCounts, resourceEntry=resourceEntry, resourceSlotIndex=resourceSlotIndex, usageDisabled=usageDisabled, resourceConfig=resourceConfig, resourceUsageEntry=resourceUsageEntry, usageBusy=usageBusy)
